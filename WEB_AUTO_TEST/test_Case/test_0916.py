# encoding: utf-8
# @author: MrZhou
# @file: test_0916.py
# @time: 2022/9/16 9:52
# @desc:unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest


class BaiDuTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.url = "https://www.baidu.com"
        self.driver.maximize_window()
        sleep(3)

    def tearDown(self):
        self.driver.close()

    def test_001(self):
        driver = self.driver
        driver.get(self.url)
        driver.find_element(By.XPATH, "//input[@id='kw']").send_keys("NBA")
        driver.find_element(By.XPATH, "//input[@id='su']").click()
        sleep(5)


if __name__ == "__main__":
    unittest.main()
