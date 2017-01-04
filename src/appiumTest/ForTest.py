# -*- coding: UTF-8 -*-
'''
Created on 2016年8月24日

@author: willie
'''
import unittest
from appiumTest.PublicClass import getMyTime,clickResourceID
import HTMLTestRunner
from appiumTest.WelcomePage import TanChuangChuLi
from appiumTest.GerenzhongxinPage import gerenzhongxin
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
        pass
        
    @classmethod
    def testGeRenZhongXin(self):
        # 如何做到自动遍历当前界面所有控件并依次点击？
        clickResourceID("net.easyconn.carman:id/id_home_main_user")
        gerenzhongxin.geren(self)

       

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    # 设置一个容器来调用将要执行的测试用例
    myunit =unittest.suite.TestSuite()
    # myunit1 使用此方法运行该类下所有的用例，执行顺序按照字母排序
    # myunit1 = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
    # 需要进行测试的用例，顺序执行
    myunit.addTest(Test("testTanChuang"))
    myunit.addTest(Test("testGeRenZhongXin"))

    # 获取当前系统时间
    mytime=getMyTime()
    myfile="C:/Users/willie/Documents/result_"+mytime+".html"
    fo = open(myfile,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(
        stream= fo,
        title='测试报告',
        description='用例执行详情'                           
    )
    runner.run(myunit)
    fo.close()