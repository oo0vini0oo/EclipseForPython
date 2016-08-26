# -*- coding: UTF-8 -*-
'''
Created on 2016年8月24日

@author: Administrator
'''

import time
from appiumTest.ForAppiumTest import findText,clickText,clickResourceID

# 如何自动监听事件是否被触发？比如权限申请

findText("下次不再提醒")
clickText("下次不再提醒")
time.sleep(2)
clickText("下次不再提醒")
time.sleep(2)
clickText("同 意")
time.sleep(2)

# 如何做到自动遍历当前界面所有控件并依次点击？
clickResourceID("net.easyconn.carman:id/iv_user")