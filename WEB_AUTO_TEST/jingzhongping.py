# encoding: utf-8
# @author: MrZhou
# @file: jingzhongping.py
# @time: 2022/9/14 12:48
# @desc:
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# from Comma import *
from selenium.webdriver.support.ui import Select
#找到浏览器对象
# driver  = webdriver.Chrome()

#访问浏览器界面
# driver.get(url)
# driver.get(url_baidu)
# sleep(3)

#跳转该frame框架内
# driver.switch_to.frame('iframeResult')

#点击alert弹窗
# driver.find_element(By.XPATH,'/html/body/input').click()

#跳转至弹框内switch_to.alert
# ele_alert=driver.switch_to.alert

#接受弹窗alert.accept
# ele_alert.accept()

#取消弹窗alert.dismiss
# ele_alert.dismiss()

#获取弹窗内文本
# print(ele_alert.text)

#向弹窗内输入文本
# ele_alert.send_keys('Byebye')

#点击登录按钮
# driver.find_element(By.ID,'s-top-loginbtn').click()
# driver.implicitly_wait(5)
# #定位登录弹窗输入框，并输入
# driver.find_element(By.XPATH,"//*[@id='TANGRAM__PSP_11__userName']").send_keys('百度')
# driver.find_element(By.ID,'TANGRAM__PSP_11__password').send_keys('12345678')
# driver.find_element(By.ID,'TANGRAM__PSP_11__submit').click()

driver = webdriver.Chrome()
driver.get("https://tieba.baidu.com/f/search/adv")
driver.maximize_window()
ele = driver.find_element(By.NAME, "sm")
time.sleep(3)
# 获取所有选项
options = Select(ele).options
print("所有选项元素：%s" % options)
print("第二个元素是:%s" % (options[1].text))
for i in options:
    print("元素分别是:" + i.text)
print("________")

# 获取下拉框当前显示选项
current = Select(ele).all_selected_options
print("当前下拉框所有选项元素:%s" % current)
print("_________")