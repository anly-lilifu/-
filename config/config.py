#coding=utf-8
"""
Author:多测师_李立伏
time:2022-02-11 17:07
Wechat:xiaoshubass
website:www.duoceshi.cn
"""
'''
此模块用来存放接口的入参信息和url以及headers


'''
# 1.登录接口的入参信息
login_url='http://cms.duoceshi.cn/cms/manage/loginJump.do'
login_data={
            'userAccount': 'admin',
            'loginPwd': '123456'
            }
login_headers={
                'Content-Type':'application/x-www-form-urlencoded'
                }
# 2.搜索admin用户的入参信息
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
# 3.打开用户管理界面的入参信息
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
# 4.进入栏目管理界面的入参信息
findCategoryByPage_url='http://cms.duoceshi.cn/cms/manage/findCategoryByPage.do'
findCategoryByPage_data={
    'Content-Type':'application/x-www-form-urlencoded'
}
findCategoryByPage_headers={
    'parentId':'',
    'categoryName':'',
    'page':'1'
}
# 5.删除用户的入参信息
userdel_url='http://cms.duoceshi.cn/cms/manage/queryUserList.do'
userdel_data={
    'startCreateDate':'',
    'endCreateDate':'',
    'searchValue':'',
    'page':'1'
}
userdel_headers={
    'Content-Type':'application/x-www-form-urlencoded'
}