#coding=utf-8
"""
Author:多测师_李立伏
time:2022-02-12 14:40
Wechat:xiaoshubass
website:www.duoceshi.cn
"""
from utils.HTMLTestRunner3_New import HTMLTestRunner
from time import strftime
import unittest
now=strftime('%Y-%m-%d_%H_%M_%S')
file=r'D:\project\cms_api_auto1\report'+'\\'+now+'_api自动化测试报告.html'
f=open(file,'wb')
start_dir=r'D:\project\cms_api_auto1\test_case'
discover=unittest.defaultTestLoader.discover(start_dir=start_dir,pattern="test*.py")
runner=HTMLTestRunner(stream=f,
                      description='用例测试执行如下',
                      tester='小李',
                      title='接口自动测试化报告'
)
runner.run(discover)