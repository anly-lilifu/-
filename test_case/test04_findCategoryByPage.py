#coding=utf-8
"""
time:2022-02-12 20:02
"""
from cms_api.cms_api import Cms
from config.config import *
import requests
import unittest
class FindCategoryByPage(Cms):
    def test04_findCategoryByPage(self):
        response=self.session.post(url=findCategoryByPage_url,data=findCategoryByPage_data,headers=findCategoryByPage_headers)
        assert response.json()
if __name__ == '__main__':
    unittest.main()
