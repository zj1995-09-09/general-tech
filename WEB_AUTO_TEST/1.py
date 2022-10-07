# encoding: utf-8
# @author: MrZhou
# @file: 1.py
# @time: 2022/9/7 16:16
# @desc:
# coding=utf-8 #
__author__ = '爱吃苹果的鱼'

    from framework.base import seleniumAction  # seleniumAction封装类引用
    from selenium import webdriver
    import time
    # driver所在路径
    driverPath = 'C:\\Users\\Administrator\\PycharmProjects\\pyTestAutomation\\framework\\driver\\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driverPath)

    driver.get('https://www.baidu.com')  # 打开百度链接
    base = seleniumAction.SeleniumActionAPI(driver)  # 初始化selenium封装类
    search_input = base.ele_get_by_id('kw')  # 获取检索输入框元素
    base.ele_send_keys(search_input, 'selenium')  # 输入框中，输入'selenium'
    base.ele_click_by_id('su')  # 点击【百度一下】搜索按钮
    time.sleep(3)
