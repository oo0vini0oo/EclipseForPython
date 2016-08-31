# -*- coding: UTF-8 -*-
'''
Created on 2016年8月24日

@author: Administrator
'''

from appium import webdriver
import time

# 连接设备
def connDevice():
    # 指定平台、启动的设备、包名和启动的activity
    desired_caps = {'platformName': 'Android', 'platformVersion': '6.0', 'deviceName': '022AUM7N49067777','appPackage': 'net.easyconn.carman', 'appActivity': '.MainActivity'}
    # 关联Appium
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver


driver = connDevice()

def getMyTime():
    mytime=time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
    
    return mytime


# 点击resourceid
def clickResourceID(resourceid):
    if driver.find_element_by_id(resourceid):   
        getScreenShot("点击该控件前的界面")
        if driver.find_element_by_id(resourceid).click() is True:
            time.sleep(1)
            getScreenShot("点击失败界面")
        else:
            time.sleep(1)
            getScreenShot("点击该控件后的界面")    
    else:
        print("未找到该控件："+resourceid)
        getScreenShot("未找到该控件")

# 点击文本
def clickText(text):
    if driver.find_element_by_name(text):
        getScreenShot("点击"+text+"前的界面")
        driver.find_element_by_name(text).click()
        time.sleep(2) 
        getScreenShot("点击"+text+"后的界面")
    else:
        print("未找到名字："+text)
        getScreenShot("未找到文本："+text)
        time.sleep(1) 

# 查找文本
def findText(text):
    if driver.find_element_by_name(text):
        getScreenShot(text)
        time.sleep(1) 
    else:
        getScreenShot("未找到文本："+text)
        time.sleep(1) 

# 截屏
def getScreenShot(filename):
    mytime=getMyTime()
    myscreenshot="C:/Users/Administrator/Documents/"+mytime+filename+".png"
    driver.get_screenshot_as_file(myscreenshot)
    


    
        
