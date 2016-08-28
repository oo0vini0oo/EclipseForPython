# -*- coding: UTF-8 -*-
'''
Created on 2016年8月24日

@author: Administrator
'''
import unittest
from appiumTest.ForAppiumTest import *
import time
import HTMLTestRunner

class Test(unittest.TestCase):

    @classmethod
    def setUp(self):
        pass

    @classmethod
    def tearDown(self):
        pass

    @classmethod
    def testName(self):
        # findText("下次不再提醒")
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
    myunit =unittest.suite.TestSuite()
    myunit.addTest(Test("testName"))
    mytime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    myfile="C:/Users/Administrator/Documents/a.html"
    fo = open(myfile,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(
        stream= fo,
        title='result',
        description='report'                             
    )
    runner.run(myunit)
    fo.close()