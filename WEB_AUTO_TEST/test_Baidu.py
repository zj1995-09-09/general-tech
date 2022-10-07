# encoding: utf-8
# @author: MrZhou
# @file: test_Baidu.py
# @time: 2022/9/7 11:20
# @desc:UI自动化
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

driver = webdriver.Chrome()
url_baidu = "https://www.baidu.com"
driver.get(url_baidu)
driver.maximize_window()
# driver.find_element(By.NAME, 'wd').send_keys("四川地震")
driver.find_element(By.XPATH, "//input[@id='kw']").send_keys("菜鸟教程")
driver.find_element(By.ID, 'su').click()
