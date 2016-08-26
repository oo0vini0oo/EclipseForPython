# -*- coding: UTF-8 -*-
'''
Created on 2016年8月24日

@author: Administrator
'''
import unittest
from appiumTest.ForAppiumTest import *
import time
class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        findText("下次不再提醒")
        clickText("下次不再提醒")
        time.sleep(2)
        clickText("下次不再提醒")
        time.sleep(2)
        clickText("同 意")
        time.sleep(2)

        # 如何做到自动遍历当前界面所有控件并依次点击？
        clickResourceID("net.easyconn.carman:id/iv_user")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()