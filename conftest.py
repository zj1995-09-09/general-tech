# encoding: utf-8
# @author: MrZhou
# @file: conftest.py
# @time: 2022/9/27 11:41
# @desc:
import pytest
import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import requests
from common.requests_handler import RequestsHandler


@pytest.fixture(name='f1')
def Login():
    print("------预制登录")


@pytest.fixture()
def driver1():
    ##前置条件
    # 1.打开浏览器
    from selenium import webdriver

    path = r'/Users/zhou/opt/anaconda3/bin/chromedriver'
    url = 'https://www.baidu.com'

    driver = webdriver.Chrome(path)
    driver.get(url)
    # 设置隐性等待 等待的时间就可以放在config中，直接参数调用
    ##方法一：放在yaml中
    # wait_time = HandlerMiddle.yaml_data["selenium"]["wait_time"]
    ##方法二、放在config.py中
    # wait_time = Wait_time
    # driver.implicitly_wait(wait_time)

    yield driver

    # 后置q清理
    driver.quit()


@pytest.fixture(scope="module", name="f2")
def driver2():
    # 1.打开乐调网站
    from selenium import webdriver
    path2 = r'/Users/zhou/opt/anaconda3/bin/chromedriver'
    # url1 = "http://192.168.10.121:81/#/login?redirect=%2Fuser%2Flist"
    url2 = "https://www.baidu.com/"

    # 2.实例化driver
    driver2 = webdriver.Chrome(path2)
    driver2.get(url2)
    driver2.maximize_window()

    yield driver2

    driver2.quit()


# @pytest.fixture(scope='module', name='f3')
# def login():
#     login_url = 'http://www.joysurvey.com:8089/survey/man/user/login'
#     payload = {
#         'phone': '18888888888', 'password': '123456789A!'
#     }
#     req = RequestsHandler()
#     res = req.visit('post', login_url, data=payload)
#     token = res['data']['token']
#
#     yield res
#     req.close_session()

# 2.1使用手机号和密码登录接口
@pytest.fixture(scope="module", name='f4')
def test_login_success():
    login_url = 'http://www.joysurvey.com:8089/survey/man/user/login'
    payload = {
        'phone': '18963988981', 'password': '123456789A!'
    }
    req = RequestsHandler()
    res = req.visit('post', login_url, data=payload)
    # global token
    token = res['data']['token']
    yield token
    req.close_session()
