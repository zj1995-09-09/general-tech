# encoding: utf-8
# @author: MrZhou
# @file: sendemail.py
# @time: 2022/9/30 12:02
# @desc:
from datetime import datetime
from pathlib import Path
from control.testcase import TestCase
from control.utils import Excel, datatodict, suite_format, mkdir
from control.log import logger
from control.data import testsuite2data
from email.mime.application import MIMEApplication
from pathlib import Path
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from control.junit import Junit
import threading


class Autotest():
    def __init__(self, parmars):

        self.parmars = parmars
        # logger.info(parmars)
        # 用例表 强转为str类型 兼容jenkins运行
        self.file_testcae = str(Path('testcase') / ('testcase.xlsx'))
        # 读取测试用例
        self.excel_testcase = Excel('r', self.file_testcae)
        # 获得用例的全部内容
        self.data = self.excel_testcase.red()
        # 转换格式为json
        self.data = datatodict(self.data)
        # 转换数据格式为测试套件返回的可执行用例json
        self.testsuit = suite_format(self.data)
        # 用于接受用例的结果
        self.result_testuite = []
        # 测试报告详细数据
        self.report_data = {}
        report_file = str(Path('report') / ('api' + '-' + 'report' + '' + '.xlsx'))
        self.report_workbook = Excel('w', report_file)
        # 生成junit测试报告
        self.junit_report = str(Path('junit') / ('api' + '-' + 'junit' + '' + '.xml'))
        # 以下为邮件配置
        self.report = str(Path('report') / ('api-report.xlsx'))

        self.send_user = '1'  # 发件人
        self.password = ''  # 授权码/密码
        self.receive_users = '@'  # 收件人，可为list
        self.subject = 'python自动化测试报告'  # 邮件主题
        self.email_text = 'hi hello this report '  # 邮件正文
        self.server_address = 'smtp.exmail.qq.com'  # 服务器地址
        self.mail_type = '1'  # 邮件类型
        # 程序开始时间
        self.start_se_time = datetime.now()
        self.junit = Junit(self.start_se_time)
        # 失败的用例
        self.step_fail = 0
        # 出错的用例
        self.step_error = 0
        # 当前时间
        self.start = datetime.now()
        # 创建文件
        files = ('report', 'junit', 'config')
        for file in files:
            mkdir(file)

        txt_path = str(Path('config') / ('txt_final.txt'))
        txt = open(txt_path, 'w')
        txt.seek(0)
        txt.truncate()
        txt.close()

    def play(self):
        # 读取测试套件执行用例
        for testcae in self.testsuit:
            # 跳过的用例
            if testcae['condition'] == 'skip':
                for skipcase in testcae['steps']:
                    logger.info(skipcase)
                    skipcase['score'] = 'skip'
                self.result_testuite.append(testcae)
                continue

                # 传入当前用例
            rcase = TestCase(testcae, self.junit)
            # 写入xml测试报告
            self.junit.case(testcae['id'], testcae['title'], datetime.now())
            # 使用线程增加运行速度
            thread = threading.Thread(target=self.result_testuite.append(rcase.run()), name=testcae['title'])
            # logger.info(thread.name)
            thread.start()
            # self.result_testuite.append(rcase.run())
            # 收到测试的结果，进行生成测试报告
        self.junit.write_toxml()

    def crateport(self):
        data = testsuite2data(self.result_testuite)
        self.report_workbook.write(data, 'repost_data')
        # 写一次就关一次
        self.report_workbook.close()

    # 发送邮箱到测试报告
    def sedEmail(self):
        # 发送邮件之前获得测试结果
        # self.email_text = '用例总数:{},'.format(len(self.result_testuite)) + '成功条数：{}'.format() + '失败条数：{}'.format(3)
        # 构造一个邮件体：正文 附件
        msg = MIMEMultipart()
        msg['Subject'] = self.subject  # 主题
        msg['From'] = self.send_user  # 发件人
        msg['To'] = self.receive_users  # 收件人

        # 构建正文
        part_text = MIMEText(self.email_text)
        msg.attach(part_text)  # 把正文加到邮件体里面去

        # 构建邮件附件
        # file = file           #获取文件路径
        part_attach1 = MIMEApplication(open(self.report, 'rb').read())  # 打开附件
        part_attach1.add_header('Content-Disposition', 'attachment', filename='1911api-report.xlsx')  # 为附件命名
        msg.attach(part_attach1)  # 添加附件

        # 发送邮件 SMTP
        smtp = smtplib.SMTP(self.server_address, 25)  # 连接服务器，SMTP_SSL是安全传输
        # smtp.set_debuglevel(1)
        smtp.login(self.send_user, self.password)
        smtp.sendmail(self.send_user, self.receive_users, msg.as_string())  # 发送邮件
        logger.info('邮件发送成功~~~~~~~~~~~~')

