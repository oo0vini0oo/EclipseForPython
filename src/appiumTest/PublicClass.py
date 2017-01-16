# -*- coding: UTF-8 -*-
'''
Created on 2016年8月24日

@author: willie
'''

from appium import webdriver
import time


# 连接设备
def connDevice():
    # 指定平台、启动的设备、包名和启动的activity
    desired_caps = {'platformName': 'Android', 'platformVersion': '6.0', 'deviceName': '217706d3','appPackage': 'net.easyconn.carman', 'appActivity': '.MainActivity'}
    # 关联Appium
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver

driver = connDevice()

def getMyTime():
    mytime=time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))    
    return mytime

# 点击resourceid
def clickResourceID(resourceid):
    try:
        if driver.find_element_by_id(resourceid):   
            getScreenShot("点击id前的界面")
            driver.find_element_by_id(resourceid).click()
            time.sleep(0.3)
            getScreenShot("点击id后的界面")
            return True
                
        else:
            print("未找到该控件："+resourceid)
            getScreenShot("未找到该控件")
            return False
    except :
        print("未找到该控件："+resourceid)
        return False    
# 点击文本
def clickText(text):
    try:
        if driver.find_element_by_name(text):
            getScreenShot("点击"+text+"前的界面")
            driver.find_element_by_name(text).click()
            time.sleep(0.3)
            getScreenShot("点击"+text+"后的界面")
            return True
        else:
            print("未找到名字："+text)
            getScreenShot("未找到文本："+text)
            return False
    except:
        print("未能点击到文本"+text)  
        return False      

# 查找文本
def findText(text):
    try:   
        if driver.find_element_by_name(text):
            getScreenShot(text)
            return True
        else:
            getScreenShot("未找到文本："+text)
            return False
    except:
        getScreenShot("未找到文本："+text)
        return False 
       

# 截屏
def getScreenShot(filename):
    mytime=getMyTime()
    myscreenshot="C:/Users/willie/Documents/"+mytime+filename+".png"
    driver.get_screenshot_as_file(myscreenshot)

#获得机器屏幕大小x,y
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
 
#屏幕向上滑动
def swipeUp(duration):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.75)   #起始y坐标
    y2 = int(l[1] * 0.25)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,duration)
#屏幕向下滑动
def swipeDown(duration):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.25)   #起始y坐标
    y2 = int(l[1] * 0.75)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,duration)
#屏幕向左滑动
def swipeLeft(duration):
    l=getSize()
    x1=int(l[0]*0.75)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.05)
    driver.swipe(x1,y1,x2,y1,duration)
#屏幕向右滑动
def swipeRight(duration):
    l=getSize()
    x1=int(l[0]*0.05)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.75)
    driver.swipe(x1,y1,x2,y1,duration)
