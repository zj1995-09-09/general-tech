# encoding: utf-8
# @author: MrZhou
# @file: qq.py
# @time: 2022/9/8 12:15
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

driver = webdriver.Chrome()

driver.get('https://mail.qq.com')
# 定位login_frame

driver.switch_to.frame("login_frame")
time.sleep(5)

# 定位账号、密码，并输入

# driver.find_element_by_xpath('//*[@id="u"]').send_keys("1587453282")
#
# driver.find_element_by_xpath('//*[@id="p"]').send_keys("199509ab")
#
# driver.find_element_by_xpath('//*[@id="login_button"]').click()
driver.find_element(By.XPATH, '//span[@id="img_out_1587453282"]').click()
driver.find_element(By.XPATH, '//*[@placeholder="请输入独立密码"]').send_keys("199509ab")
# 定位登录按钮

driver.find_element(By.XPATH, '//*[@id="login_button"]').click()
