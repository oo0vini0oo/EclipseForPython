# -*- coding: UTF-8 -*-
'''
Created on 2016年8月24日

@author: willie
'''
import unittest
from appiumTest.PublicClass import getMyTime,clickResourceID,swipeLeft,swipeRight,getScreenShot
import HTMLTestRunner
from appiumTest.WelcomePage import TanChuangChuLi
from appiumTest.GerenzhongxinPage import gerenzhongxin
import time
from appiumTest.ThreeApp import threeAppTest
from appiumTest.Map import mymap
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

        swipeLeft(1000)
        time.sleep(1.5)
        getScreenShot("swipe left")
        swipeRight(1000)
        time.sleep(0.5)
        getScreenShot("swipe right")

     
    @classmethod
    def testMianZeShengMing(self):
        pass
        
    @classmethod
    def testClickuser(self):
        # 如何做到自动遍历当前界面所有控件并依次点击？
        clickResourceID("net.easyconn.carman:id/id_home_main_user")
    
    @classmethod
    def testGeren(self):     
        gerenzhongxin.denglu(self)
        
    @classmethod
    def testYemian(self):     
        gerenzhongxin.yemian(self)
    
    @classmethod
    def testShezhi(self):     
        gerenzhongxin.shezhi(self)   

    @classmethod
    def testFeedback(self):     
        gerenzhongxin.feedback(self)
        
    @classmethod
    def testAbout(self):     
        gerenzhongxin.about(self)
    
    @classmethod
    def testThreeApp(self):     
        threeAppTest.threeApp(self)
           
    @classmethod
    def testMap(self):
        mymap.mySearchtext(self)
        
if __name__ == "__main__":

    # 设置一个容器来调用将要执行的测试用例
    myunit =unittest.suite.TestSuite()
    # myunit1 使用此方法运行该类下所有的用例，执行顺序按照字母排序
    # myunit1 = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
    # 需要进行测试的用例，顺序执行
    myunit.addTest(Test("testTanChuang"))
#     myunit.addTest(Test("testClickuser"))
#     myunit.addTest(Test("testGeren"))
#     myunit.addTest(Test("testYemian"))
#     myunit.addTest(Test("testShezhi"))
#     myunit.addTest(Test("testFeedback"))
#     myunit.addTest(Test("testAbout"))
#     myunit.addTest(Test("testThreeApp"))
    myunit.addTest(Test("testMap"))
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