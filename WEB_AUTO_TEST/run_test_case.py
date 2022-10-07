# encoding: utf-8
# @author: MrZhou
# @file: test_Case.py
# @time: 2022/9/16 10:58
# @desc:testcase

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
import os

# from test_0916 import BaiDuTest

# 测试套件
# suite = unittest.TestSuite()

# 加载测试用例

current_path = os.path.dirname(os.path.abspath(__file__))
case_path = os.path.join(current_path, "test_Case")
# case_dir = "./test_Case/"

discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
# suite.addTest(discover)
# suite.addTest(BaiDuTest("test_001"))
# discover=unittest.TestLoader.loadTestsFromTestCase()


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(discover)
    # unittest.main(defaultTest="suite")

