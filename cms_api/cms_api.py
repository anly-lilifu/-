#coding=utf-8
"""
Author:多测师_李立伏
time:2022-02-11 17:10
Wechat:xiaoshubass
website:www.duoceshi.cn
"""
from config.config import *
import  requests
class Cms:
    def __init__(self):
        self.session=requests.Session()
    def login(self):
        respsonse=self.session.post(url=login_url,data=login_data,headers=login_headers)
        return respsonse.json()
    def queryUserList(self):
        response=self.session.post(url=query_url,data=query_data,headers=query_headers)
        return response.json()
    def queryUserList1(self):
        response=self.session.post(url=queryUser_url,data=queryUser_data,headers=queryUser_headers)
        return response.json()
    def findCategoryByPage(self):
        response=self.session.post(url=findCategoryByPage_url,data=findCategoryByPage_data,headers=findCategoryByPage_headers)
        return response.json()
    def userdel(self):
        response=self.session.post(url=userdel_url,data=userdel_data,headers=userdel_headers)
        return response.json()
if __name__ == '__main__':
    c=Cms
    c.login()
    c.queryUserList()
    c.queryUserList1()


