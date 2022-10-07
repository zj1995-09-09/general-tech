"""
项目入口，主程序。
收集用例，运行用例，生成报告。
"""
import os
import pytest
from config import path
from datetime import datetime
# pytest 收集用例，
# 如何放到 reports
# reports/report.html

# 获取现在的时间戳
ts = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
report_file_name = 'report' + ts + '.html'
# 获取测试报告存储目录
pytest.main(['--html={}'.format(report_file), '-s'])
report_dir = path.reports_path
# # 拼接文件
report_file = os.path.join(report_dir, report_file_name)
print(report_file)

