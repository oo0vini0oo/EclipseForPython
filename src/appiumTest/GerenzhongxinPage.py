# -*- coding: UTF-8 -*-
'''
Created on 2017年1月4日

@author: willie
'''


'''
    net.easyconn.carman:id/iv_system_back 返回
    net.easyconn.carman:id/ci_user_icon
    net.easyconn.carman:id/tv_nick_name  登录
    
    net.easyconn.carman:id/rl_system_settings 设置
    net.easyconn.carman:id/rl_system_feedback 反馈
    net.easyconn.carman:id/rl_system_about 关于


'''

from appiumTest.PublicClass import clickResourceID,clickText
import time

class gerenzhongxin():
    def geren(self):
        clickResourceID("net.easyconn.carman:id/tv_nick_name")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        clickText("我的足迹")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        clickText("离线地图")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        clickText("汽车互联")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        clickText("连接方控")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        clickText("里程排行")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        clickText("路况提醒")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        clickText("胎压检测")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
            
        ''' 
        net.easyconn.carman:id/cb_screen_always_on
        net.easyconn.carman:id/welcom_xiaoyi_cb
        net.easyconn.carman:id/cb_auto_playing_music
        net.easyconn.carman:id/tv_music_control
        
        net.easyconn.carman:id/rb_auto
        net.easyconn.carman:id/rb_night
        net.easyconn.carman:id/rb_light
        
        net.easyconn.carman:id/tv_navi_setting
        net.easyconn.carman:id/tv_wrc_setting
        '''      
        clickResourceID("net.easyconn.carman:id/rl_system_settings")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/cb_screen_always_on")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/welcom_xiaoyi_cb")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/cb_auto_playing_music")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/tv_music_control")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/rb_light")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/tv_navi_setting")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/rb_night")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/tv_wrc_setting")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/cb_screen_always_on")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/welcom_xiaoyi_cb")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/cb_auto_playing_music")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/rb_auto")
        time.sleep(1)
        
        
        
        
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/rl_system_feedback")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/rl_system_about")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
        time.sleep(1)
        clickResourceID("net.easyconn.carman:id/iv_system_back")
    
    