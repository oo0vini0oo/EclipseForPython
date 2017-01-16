# -*- coding: UTF-8 -*-
'''
Created on 2016年8月24日

@author: willie
'''

'''
此类用来处理系统弹窗，各种权限
但是优先执行

'''

from appiumTest.PublicClass import clickText


class TanChuangChuLi(): 
#     def tanChuang(self):
#         myBoolean=True
#         while myBoolean:   
#             try:
#                 if findText("写入/删除短信"):
#                     clickText("允许") 
#                     continue  
#                 elif findText("读取联系人"):
#                     clickText("允许")
#                     continue
#                 elif findText("读取位置信息"):
#                     clickText("允许")
#                     continue
#                 elif findText("读取通话记录"):
#                     clickText("允许")
#                     continue
#                 elif findText("读取已安装应用列表"):
#                     clickText("同 意")
#                     continue
#                 elif findText("启用录音"):                                                                                                                                                  
#                     clickText("同 意")
#                     continue
#                 elif findText("免责声明"):
#                     clickText("同 意")
#                     continue
#                 elif findText("跳过"):
#                     clickText("跳过")
#                     continue
#                 elif findText("喜欢亿连吗?去应用市场给个评分吧!~求鼓励~求鼓励~ (^_^)"):
#                     clickText("不喜欢")
#                     continue
#                 elif clickResourceID("net.easyconn.carman:id/home_app_guide_view"):
#                     continue
#                 else:
#                     print("未弹出权限处理")   
#                     myBoolean=False     
#             except:
#                 print("捕获到异常")
#                 continue
#         else:
#             print("退出弹框处理")

    def tanChuangOne(self):
        myBoolean=True
        while myBoolean:   
            try:
                if clickText("允许"):                        
                    continue                                      
                elif clickText("跳过"):                        
                    continue
                elif clickText("同 意"):                        
                    continue
                elif clickText("不喜欢"):                        
                    continue
                else:
                    print("未弹出权限处理")   
                    myBoolean=False     
            except:
                print("捕获到异常")
                continue
        else:
            print("退出弹框处理")