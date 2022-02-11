#coding=utf-8
"""
Author:多测师_李立伏
time:2022-02-11 9:09
Wechat:xiaoshubass
website:www.duoceshi.cn
"""
import requests

# longin_url='http://cms.duoceshi.cn/cms/manage/loginJump.do'
# longin_data={
#     'userAccount': 'admin',
#     'loginPwd': '123456'
# }
# longin_headers={
#     'Content-Type': 'application/x-www-form-urlencoded'
# }
# response=requests.request('post',url=longin_url,data=longin_data,headers=longin_headers)
# print(response)
# print(response.text,type(response.text))
# print(response.headers)
# print((response.cookies))
# print(response.request)
# print(response.elapsed)
# print(response.status_code)

# longin_url='http://cms.duoceshi.cn/cms/manage/loginJump.do'
# longin_data={
#     'userAccount': 'admin',
#     'loginPwd': '123456'
# }
# response=requests.request('get',url=longin_url,params=longin_data)
# print(response)
# print(response.text,type(response.text))
# print(response.headers)
# print((response.cookies))
# print(response.request)
# print(response.elapsed)
# print(response.status_code)

# class Cms(object):
#     def __init__(self):
#         self.session=requests.Session()
#     def login(self):
#         longin_url = 'http://cms.duoceshi.cn/cms/manage/loginJump.do'
#         longin_data={
#             'userAccount': 'admin',
#             'loginPwd': '123456'
#         }
#         longin_headers={
#             'Content-Type': 'application/x-www-form-urlencoded'
#         }
#         response=self.session.post(url=longin_url,headers=longin_headers,data=longin_data)
#         result=response.json()
#         # print(result)
#         if result['msg']=='登录成功！':
#             print("登录接口调试成功")
#         else:
#             print('登录接口调试失败')
#     def queryUserList(self):
#         queryUserList_url='http://cms.duoceshi.cn/cms/manage/queryUserList.do'
#         queryUserList_headers={
#             'Content - Type': 'application / x - www - form - urlencoded'
#         }
#         queryUserList_data={
#             'startCreateDate':'',
#             'endCreateDate':'',
#             'searchValue':'',
#             'page': '1'
#         }
#         response=self.session.post(url=queryUserList_url,headers=queryUserList_headers,data=queryUserList_data)
#         result=response.json()
#         # print(result)
#         if result['msg']== '查询用户成功！':
#             print('查询用户接口调用成功')
#         else:
#             print('查询用户接口调用失败')
# if __name__ == '__main__':
#     c=Cms()
#     c.login()
#     c.queryUserList()


import  re
# class Prvince(object):
#     def get_prvince(self):
#         prvince_url='http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getSupportProvince'
#         response=requests.get(url=prvince_url)
#         result=response.text
#         print(result)
#
#
#
# if __name__ == '__main__':
#     p=Prvince()
#     p.get_prvince()

# class Yshop(object):
#     def get_uuid(self):
#         uuid_url='http://manage.duoceshi.com/auth/code'
#         response=requests.get(url=uuid_url)
#         # print(response.json()['uuid'])
#         return response.json()["uuid"]
#     def longin(self):
#         longin_url='http://manage.duoceshi.com/auth/login'
#         longin_headers={
#             'Content-Type':'application/json'
#         }
#         longin_json={
#             "username": "admin",
#             "password": "q8TjyUth/POUk9ABvlHR1jW9jO2JZUo2DjqSxg6fc5ytqf7DWpoORD0DNZYvEkVQ5zw9BifWJWpHSAhGjtnD2g==",
#             "code": "8888",
#             "uuid": self.get_uuid()
#         }
#         response=requests.post(url=longin_url,headers=longin_headers,json=longin_json)
#         return response.json()['token']
#     def querystore(self):
#         query_url='http://manage.duoceshi.com/api/yxUser?page=0&size=10&sort=uid%2Cdesc&userType='
#         query_headers={
#             "Authorization": self.longin()
#         }
#         reponse=requests.get(url=query_url,headers=query_headers)
#         print(reponse.text)
# if __name__ == '__main__':
#     y=Yshop()
#     # y.get_uuid()
#     # y.longin()
#     y.querystore()



import  unittest
class Cms_api(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session=requests.Session()
    def test01_login(self):
        login_url='http://cms.duoceshi.cn/cms/manage/loginJump.do'
        login_data={
            'userAccount': 'admin',
            'loginPwd': '123456'
        }
        login_headers={
            'Content-Type':'application/x-www-form-urlencoded'
        }
        respsonse=self.session.post(url=login_url,data=login_data,headers=login_headers)
        reslut=respsonse.json()
        assert reslut["msg"]== "登录成功！"
    def test02_queryUserList(self):
        query_url='http://cms.duoceshi.cn/cms/manage/queryUserList.do'
        query_headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        query_data={
            'startCreateDate':'',
            'endCreateDate':'',
            'searchValue': 'admin',
            'page': '1'
        }
        response=self.session.post(url=query_url,data=query_data,headers=query_headers)
        reslut=response.json()
        assert  reslut['msg']== "查询用户成功！"
    def test03_queryUserList1(self):
        queryUser_url='http://cms.duoceshi.cn/cms/manage/queryUserList.do'
        queryUser_data={
            'startCreateDate':'',
            'endCreateDate':'',
            'searchValue':'',
            'page':'1'
        }
        queryUser_headers={
            'Content - Type': 'application / x - www - form - urlencoded'
        }
        response=self.session.post(url=queryUser_url,data=queryUser_data,headers=queryUser_headers)
        reslut=response.json()
        assert reslut["msg"]=='查询用户成功！'



if __name__ == '__main__':
    unittest.main()