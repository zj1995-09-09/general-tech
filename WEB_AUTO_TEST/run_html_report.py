# encoding: utf-8
# @author: MrZhou
# @file: run_html_report.py
# @time: 2022/9/16 16:29
# @desc:
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

from test_Case import test_0011

import time
from HTMLTestRunner import HTMLTestRunner

import unittest

# 组装测试套件
suite = unittest.TestSuite()

# 通过测试套件加载测试用例
suite.addTest(test_0011.Login("test01"))
suite.addTest(test_0011.Login("test02"))
suite.addTest(test_0011.Login("test03"))

if __name__ == '__main__':
    # 定义一个测试文件名称
    now = time.strftime("%Y-%m-%d--%H-%M-%S")

    # 定义报告存放路径
    file_Report = './Report/' + now + "_result.html"

    # 创建该报告文件
    fp = open(file_Report, 'wb')


    # 定义测试报告
    runner = HTMLTestRunner(
        stream=fp,
        title="测试报告",
        description="用例执行情况"
    )

    runner.run(suite)

    # 关闭报告文件
    fp.close()
