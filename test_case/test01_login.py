#coding=utf-8
"""
Author:多测师_李立伏
time:2022-02-12 14:41
Wechat:xiaoshubass
website:www.duoceshi.cn
"""
import unittest
from cms_api.cms_api import Cms
import requests
from config.config import *
class login(Cms):
    @classmethod
    def setUpClass(cls) -> None:
        Cms.set_session()
    def test01_login(self):
        response=self.session.post(url=login_url,data=login_data,headers=login_headers)
        assert response.json()["msg"]=='登录成功！'

if __name__ == '__main__':
    unittest.main()