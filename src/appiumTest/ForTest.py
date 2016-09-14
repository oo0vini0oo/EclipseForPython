# -*- coding: UTF-8 -*-
'''
Created on 2016年8月24日

@author: Administrator
'''
import unittest
from appiumTest.PublicClass import *
import time
import HTMLTestRunner
from appiumTest.WelcomePage import TanChuangChuLi

class Test(unittest.TestCase):
  
    @classmethod
    def setUp(self):
        pass

    @classmethod
    def tearDown(self):
        pass
    
    @classmethod
    def testTanChuang(self):
        TanChuangChuLi.tanChuangOne(self)
       # TanChuangChuLi.clickAlert(self)
            
    @classmethod
    def testMianZeShengMing(self):

        findText("免责声明")
        
        time.sleep(2)       
       
    @classmethod
    def testBuZaiTiXing(self):
        clickText("下次不再提醒")
        time.sleep(2)
        clickText("下次不再提醒")
        time.sleep(2)
        clickText("同 意")
        time.sleep(2)    
        
    @classmethod
    def testGeRenZhongXin(self):
        # 如何做到自动遍历当前界面所有控件并依次点击？
        clickResourceID("net.easyconn.carman:id/iv_user")
       

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    # 设置一个容器来调用将要执行的测试用例
    myunit =unittest.suite.TestSuite()
    # myunit1 使用此方法运行该类下所有的用例，执行顺序按照字母排序
    # myunit1 = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
    # 需要进行测试的用例，顺序执行
#    myunit.addTest(Test("testTanChuang"))
    myunit.addTest(Test("testTanChuang"))
#     myunit.addTest(Test("testBuZaiTiXing"))         
    myunit.addTest(Test("testGeRenZhongXin"))
    # 获取当前系统时间
    mytime=getMyTime()
    myfile="C:/Users/Administrator/Documents/result_"+mytime+".html"
    fo = open(myfile,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(
        stream= fo,
        title='测试报告',
        description='用例执行详情'                           
    )
    runner.run(myunit)
    fo.close()