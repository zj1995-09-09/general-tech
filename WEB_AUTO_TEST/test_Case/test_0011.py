# encoding: utf-8
# @author: MrZhou
# @file: test_0011.py
# @time: 2022/9/15 11:49
# @desc:unit

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from time import sleep


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("start__")

    @classmethod
    def tearDownClass(cls):
        print("end___")

    # @unittest.skipIf(1, "条件成立则跳过")
    def test01(self):
        print("第一条用例")

    @unittest.expectedFailure
    def test02(self):
        print("第二条用例")

    def test03(self):
        print("第三条用例")


if __name__ == "__main__":
    unittest.main()
