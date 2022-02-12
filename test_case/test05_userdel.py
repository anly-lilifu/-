#coding=utf-8
"""
time:2022-02-12 20:09
"""
from cms_api.cms_api import Cms
from config.config import *
import requests
import unittest
class Userdel(Cms):
    def test05_userdel(self):
        responers=self.session.post(url=userdel_url,data=userdel_data,headers=userdel_headers)
        assert responers.json()['msg']=='查询用户成功！'

if __name__ == '__main__':
    unittest.main()