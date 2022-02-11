#coding=utf-8
"""
Author:多测师_李立伏
time:2022-02-11 19:07
Wechat:xiaoshubass
website:www.duoceshi.cn
"""
import unittest
import requests
from cms_api.cms_api import Cms
class Cms_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cms=Cms()
    def test01_login(self):
        assert self.cms.login()['msg']=='登录成功！'
    def test02_queryUserList(self):
        assert self.cms.queryUserList1()['msg']=='查询用户成功！'
    def test03_queryUserList1(self):
        assert self.cms.queryUserList1()['msg']=='查询用户成功！'
    def test04_findCategoryByPage(self):
        assert self.cms.findCategoryByPage()['msg']=='查询栏目成功'
    def test05_userdel(self):
        assert self.cms.userdel()["msg"]=='查询用户成功！'
if __name__ == '__main__':
    unittest.main()
