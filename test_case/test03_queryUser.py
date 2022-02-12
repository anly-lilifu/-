#coding=utf-8
"""
time:2022-02-12 16:16
"""
from cms_api.cms_api import Cms
from config.config import *
import requests
import unittest
class QueryUser(Cms):
    def test03_queryUser(self):
        response=self.session.post(url=queryUser_url,data=queryUser_data,headers=queryUser_headers)
        assert response.json()['msg']=='查询用户成功！'
if __name__ == '__main__':
    unittest.main()

