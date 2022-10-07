# encoding: utf-8
# @author: MrZhou
# @file: 6.py
# @time: 2022/9/8 15:07
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
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://news.baidu.com/")
driver.maximize_window()
time.sleep(3)
# js方法滑动滚动条
js_Scroll = "document.documentElement.scrollTop=1000"
driver.execute_script(js_Scroll)

# driver = webdriver.Chrome()
# driver.get("https://www.1000.com/")
# driver.maximize_window()
# driver.find_element(By.XPATH, "//input[@id='nickName0']").send_keys("13075509378")
# driver.find_element(By.XPATH, "//input[@id='logPsw']").send_keys("199509ab")
# driver.find_element(By.XPATH,
#                     "//body/div[@id='react-content']/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[5]/div[2]/div[1]/span[1]/input[1]").click()
# driver.find_element(By.XPATH,
#                     "//body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/button[1]/span[1]").click()

# all_cookies = driver.get_cookies()
# print(all_cookies)
#
# driver.delete_cookie("a9a68f4fefd3b693f10be4a89799dc48")
# all_cookies2 = driver.get_cookies()
# 第一种
# for i in all_cookies2:
#     if i["name"] == "a9a68f4fefd3b693f10be4a89799dc48":
#         print(i + "你还没被删掉")
#         break
#     else:
#         print("已经删干净了呢,现在cookie是" + str(i))
# 第二种
# cookie2 = driver.get_cookie("a9a68f4fefd3b693f10be4a89799dc48")
# print(cookie2)

# ele = driver.find_element(By.NAME, "sm")
# time.sleep(3)
# Select(ele).select_by_index(2)
# time.sleep(2)
# Select(ele).select_by_value("0")
# time.sleep(2)
# Select(ele).select_by_visible_text("按时间顺序")

# 获取所有选项
# options = Select(ele).options
# print("所有选项元素：%s" % options)
# print("第二个元素是:%s" % (options[1].text))
# for i in options:
#     print("元素分别是:" + i.text)
# print("________")

# 获取下拉框当前显示选项
# current = Select(ele).all_selected_options
# print("当前下拉框所有选项元素:%s" % current)
# print("_________")

# 获取第一个
# first = Select(ele).first_selected_option
# print("第一个是:%s" % (first.text))
# driver.find_element(By.XPATH, "//a[@id='s-top-loginbtn']").click()
# driver.implicitly_wait(5)
# driver.find_element(By.XPATH, "//input[@id='TANGRAM__PSP_11__userName']").send_keys("18130124923")
# driver.find_element(By.XPATH, "//input[@id='TANGRAM__PSP_11__password']").send_keys("199509ab")
# driver.find_element(By.XPATH, "//input[@id='TANGRAM__PSP_11__submit']").click()

# driver.switch_to.frame("iframeResult")
# driver.find_element(By.XPATH, '//input[@value="显示提示框"]').click()
# time.sleep(3)
# ele = driver.switch_to.alert
# ele.accept()

# driver.switch_to.frame(0)
# driver.switch_to.frame(driver.find_elements(By.TAG_NAME,"iframe")[0])

# driver.find_element(By.XPATH, "//input[@name='email']").send_keys("13075509378")
# driver.find_element(By.XPATH, "//input[@name='password']").send_keys("199509abZJ")
# driver.find_element(By.ID, "dologin").click()

# driver.get("https://www.baidu.com")
# driver.find_element(By.LINK_TEXT, "图片").click()
# all = driver.window_handles
# print("所有句柄有%s" % all)
# print("---")
# print("当前句柄是%s" % (driver.current_window_handle))
# print("----")
# driver.switch_to.window(all[1])
# print("现在的句柄是%s" % (driver.current_window_handle))
# print("懂了吗")

# driver.get('file:///E:/KT03/0913%E5%91%A8%E4%BA%8C%E7%AE%80%E5%8E%86/slider.html')
# driver.maximize_window()
# driver.find_element(By.XPATH, "//input[@id='id_username']").send_keys("ZHOUJIAN")
# driver.find_element(By.XPATH, "//input[@id='id_username']").send_keys(Keys.CONTROL, "a")
# time.sleep(2)
# driver.find_element(By.XPATH, "//input[@id='id_username']").send_keys(Keys.CONTROL, "x")
# time.sleep(2)
# driver.find_element(By.XPATH, "//input[@id='id_username']").send_keys(Keys.CONTROL, "v")
# time.sleep(2)
# driver.close()
# driver.find_element(By.XPATH, '//input[@id="su"]').click()
# 滑轨
# huagui = driver.find_element(By.XPATH, '//div[contains(text(),"滑动解锁")]')
# huagui_size = huagui.size
# print("滑轨的大小是:" + str(huagui_size))

# 滑块
# huakuai = driver.find_element(By.XPATH, '//body/form[@id="login-form"]/div[@id="box"]/div[3]/i[1]')
# huakuai_location = huakuai.location
# print("滑块的坐标是：" + str(huakuai_location))
# switch_to.frame(参数)  可以填三种值 frame_id frame_name
# 如果frame没有id/name参数，那最好的做法是定位标签名：
# driver.get('https://126.com/')
# element_frame = driver.find_element(By.XPATH,
#                                     '//iframe[@src="https://passport.126.com/webzj/v1.0.1/pub/index_dl2_new.html?cd=%2F%2Fmimg.127.net%2Fp%2Ffreemail%2Findex%2Funified%2Fstatic%2F2022%2F%2Fcss%2F&amp;cf=urs.126.bf0d9d58.css&amp;MGID=1662626284846.1526&amp;wdaId=&amp;pkid=QdQXWEQ&amp;product=mail126"]')  # 定位iframe的标签名
# driver.switch_to.frame(element_frame)  # 跳进框架内部的html
# driver.find_element(By.XPATH, '//input[@placeholder="邮箱账号或手机号码"]').send_keys("123")
# time.sleep(5)

# driver.get('https://www.tmall.com/')
# driver.find_element(By.XPATH,'//span[contains(text(),"女装")]').click()
# time.sleep(5)
# driver.quit()

# driver.get('https://www.baidu.com')
# driver.find_element(By.XPATH, '//input[@id="su"]').click()
# tupian = driver.find_element(By.LINK_TEXT, "图片")
# ActionChains(driver).move_to_element(tupian).perform()
# ActionChains(driver).context_click(tupian).perform()
# time.sleep(5)
# print(driver.current_url)
# print(driver.title)
# print(driver.name)
# print(driver.page_source)
# driver.quit()

# driver.get('file:///E:/KT03/0913%E5%91%A8%E4%BA%8C%E7%AE%80%E5%8E%86/slider.html')
# driver.maximize_window()
# driver.find_element(By.XPATH, '//input[@id="su"]').click()
# 滑轨
# huagui = driver.find_element(By.XPATH, '//div[contains(text(),"滑动解锁")]')
# huagui_size = huagui.size
# print("滑轨的大小是:" + str(huagui_size))

# 滑块
# huakuai = driver.find_element(By.XPATH, '//body/form[@id="login-form"]/div[@id="box"]/div[3]/i[1]')
# huakuai_location = huakuai.location
# print("滑块的坐标是：" + str(huakuai_location))

# 坐标
# x_location = huagui_size["width"]
# y_location = huagui_size['height']

# ActionChains(driver).drag_and_drop_by_offset(huakuai, huagui_size["width"], huagui_size['height']).perform()

# driver.get('https://www.1000.com/')
# ele_shouji = driver.find_element(By.XPATH, '//input[@id="nickName0"]')
# time.sleep(5)
# print(ele_shouji.get_attribute("placeholder"))

# coding=utf-8
# from selenium import webdriver
# import time

# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com/")
# nowhandle = driver.current_window_handle  # 获得当前窗口
# driver.find_element(By.LINK_TEXT, "贴吧").click()  # 打开贴吧新窗口
# allhandles = driver.window_handles  # 如果是打开2个新的窗口则返回所有打开的窗口
# for handle in allhandles:  # 遍历所有窗口
#     if handle != nowhandle:
#         driver.switch_to_win(handle)
#         print("switch back windows !")
#         driver.find_element(By.ID, "wd1").sendkeys(u"在贴吧中搜索")
#         time.sleep(5)
#         driver.close()
# driver.switch_to(nowhandle)  # 回到原先的窗口driver.back ()
# driver.find_element(By.ID, "kw").send_keys(u"注册成功!")
# time.sleep(3)
# driver.quit()
