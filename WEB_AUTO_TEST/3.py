# encoding: utf-8
# @author: MrZhou
# @file: 3.py
# @time: 2022/9/7 16:30
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


def test_cainiaojiaocheng():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    driver.set_window_size(1552, 840)
    driver.find_element(By.ID, "kw").click()
    driver.find_element(By.ID, "kw").send_keys("菜鸟教程")
    driver.find_element(By.ID, "kw").send_keys(Keys.ENTER)
    # element = driver.find_element(By.XPATH, "//div[@id=\'1\']/div/div/div[2]/div/div[2]/div/a/span")
    # actions = ActionChains(driver)
    # actions.move_to_element(element).perform()
    # self.vars["window_handles"] = driver.window_handles
    driver.find_element(By.PARTIAL_LINK_TEXT, "- 学的不仅是技术,更是梦").click()
    # self.vars["win7926"] = self.wait_for_window(2000)
    driver.switch_to.window(self.vars["win7926"])
    driver.find_element(By.ID, "s").click()
    driver.find_element(By.ID, "s").send_keys("python")
    # self.vars["window_handles"] = driver.window_handles
    driver.find_element(By.ID, "s").send_keys(Keys.ENTER)
    # self.vars["win7925"] = self.wait_for_window(2000)
    # driver.switch_to.window(self.vars["win7925"])


print(test_cainiaojiaocheng())
