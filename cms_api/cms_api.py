#coding=utf-8
"""
Author:多测师_李立伏
time:2022-02-12 14:39
Wechat:xiaoshubass
website:www.duoceshi.cn
"""
'''
装配置文件
'''
from config.config import *
import requests
import unittest
class Cms(unittest.TestCase):
    @classmethod
    def set_session(cls) -> None:
        cls.session=requests.Session()
    # def get_session(cls) -> None:
    #     cls.session=requests.Session
    #     return set.session


