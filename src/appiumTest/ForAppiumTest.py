# -*- coding: UTF-8 -*-
'''
Created on 2016年8月24日

@author: Administrator
'''

from appium import webdriver


# 连接设备
def connDevice():
    # 指定平台、启动的设备、包名和启动的activity
    desired_caps = {'platformName': 'Android', 'platformVersion': '4.4', 'deviceName': '217706d3',
                    'appPackage': 'net.easyconn.carman', 'appActivity': '.MainActivity'}
    # 关联Appium
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver


driver = connDevice()

# 点击resourceid
def clickResourceID(resourceid):
    if driver.find_element_by_id(resourceid):
        driver.find_element_by_id(resourceid).click()
    else:
        print("未找到该控件：" + resourceid)

# 点击文本
def clickText(text):
    if driver.find_element_by_name(text):
        driver.find_element_by_name(text).click()
    else:
        print("未找到名字：" + text)

# 查找文本
def findText(text):
    if driver.find_element_by_name(text):
        print('找到文本：' + text)
    else:
        print("未找到文本：" + text)
