#coding=utf-8
"""
time:2022-02-12 16:00
"""
from cms_api.cms_api import Cms
from config.config import *
import requests
import unittest
class Query(Cms):
    def test02_query(self):
        response=self.session.post(url=query_url,headers=query_headers,data=query_data)
        assert response.json()['msg']=='查询用户成功！'
if __name__ == '__main__':
    unittest.main()