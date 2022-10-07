# encoding: utf-8
# @author: MrZhou
# @file: 5.py
# @time: 2022/9/7 17:20
# @desc:
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest


class TestSichuan(unittest.TestCase):
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        time.sleep(5)
        self.driver.quit()

    # def wait_for_window(self, timeout=2):
    #     time.sleep(round(timeout / 1000))
    #     wh_now = self.driver.window_handles
    #     wh_then = self.vars["window_handles"]
    #     if len(wh_now) > len(wh_then):
    #         return set(wh_now).difference(set(wh_then)).pop()

    def test_sichuan(self):
        self.setup_method('')
        self.driver.get("https://www.baidu.com/")
        self.driver.set_window_size(1552, 840)
        self.driver.find_element(By.ID, "kw").send_keys("四川地震")
        self.driver.find_element(By.ID, "kw").send_keys(Keys.ENTER)
        # element = self.driver.find_element(By.CSS_SELECTOR, ".banner-pic_2ofWj .is-cover_2MND3")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # element = self.driver.find_element(By.CSS_SELECTOR, "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        # element = self.driver.find_element(By.LINK_TEXT, "四川泸定发生6.8级地震")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # element = self.driver.find_element(By.CSS_SELECTOR, "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        # element = self.driver.find_element(By.LINK_TEXT, "四川泸定地震已致74人遇难：甘孜州40人，雅安市34人")
        actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # self.vars["window_handles"] = self.driver.window_handles
        # self.driver.find_element(By.LINK_TEXT, "四川泸定地震已致74人遇难：甘孜州40人，雅安市34人").click()
        # self.vars["win3270"] = self.wait_for_window(2000)
        # self.vars["root"] = self.driver.current_window_handle
        # self.driver.switch_to.window(self.vars["win3270"])
        # self.driver.switch_to.window(self.vars["root"])
        # element = self.driver.find_element(By.CSS_SELECTOR, "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        # self.driver.switch_to.window(self.vars["win3270"])
        # element = self.driver.find_element(By.LINK_TEXT, "红星新闻")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # self.driver.execute_script("window.scrollTo(0,196)")
        # self.driver.execute_script("window.scrollTo(0,1000)")
        self.teardown_method('')


if __name__ == '__main__':
    unittest.main()
