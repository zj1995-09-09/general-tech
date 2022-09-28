# encoding: utf-8
# @author: MrZhou
# @file: run_beautiful_report.py
# @time: 2022/9/27 11:43
# @desc:

from selenium.webdriver.common.by import By
import unittest
import time
from BeautifulReport import BeautifulReport
import os

# 组装测试套件
# suite = unittest.TestSuite()

# 通过测试套件加载测试用例
# suite.addTest(test_0011.Login("test01"))
# suite.addTest(test_0011.Login("test02"))
# suite.addTest(test_0011.Login("test03"))

# test_dir="./"
current_path = os.path.dirname(os.path.abspath(__file__))
case_path = os.path.join(current_path, "test_Case")

discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")

if __name__ == '__main__':
    # 定义一个测试文件名称
    now = time.strftime("%Y-%m-%d--%H-%M-%S")

    # 定义报告存放路径
    file_location = './Report/' + now + "beautiful.html"

    # 创建该报告文件
    test_report = BeautifulReport(discover)

    test_report.report(
        filename=file_location,
        description="测试报告",
        theme="theme_default",
        report_dir="."

    )
