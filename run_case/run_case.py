#coding=utf-8
"""
Author:多测师_李立伏
time:2022-02-11 19:06
Wechat:xiaoshubass
website:www.duoceshi.cn
"""
from utils.HTMLTestRunner3_New import HTMLTestRunner
from time import strftime
import unittest
now=strftime('%Y-%m-%d_%H_%M_%S')
file=r"D:\cms_api_auto\report"+"\\"+now+"_api自动化测试报告.html"
f=open(file,'wb')
start_dir=r"D:\cms_api_auto\test_case"
discover=unittest.defaultTestLoader.discover(start_dir=start_dir,pattern="test*.py")
runner=HTMLTestRunner(stream=f,
                      description='用例情况执行如下',
                      tester='小李',
                      title='接口自动化测试报告'
                    )
runner.run(discover)