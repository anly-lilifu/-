#coding=utf-8
'''
此模块用来装页面的元素定位的文本

'''''

class  Page_elem(object):
    #1.1.登录账号元素
    userName = ["id", "userAccount"]
    #1.2.登录密码元素
    passwd = ["id", "loginPwd"]
    #1.3.登录按钮元素
    loginbtn = ["id", "loginBtn"]
    #3.1.添加用户元素
    adduser = ["link_text", "添加用户"]
    #3.2.输入用户姓名元素
    adduseranme = ['xpath', '//*[@id="userName"]']
    #3.3.性别确认元素
    sex = ['xpath', '//*[@id="userSex"]']
    #3.4.输入手机号元素
    cellphone = ['xpath', '//*[@id="user-tel"]']
    # 3.5输入邮箱元素
    mailbox = ['xpath', '//*[@id="user-email"]']
    # 3.6输入用户名元素
    id = ['xpath', '//*[@id="userAccount"]']
    # 3.7输入密码元素
    password = ['xpath', '//*[@id="loginPwd"]']
    # 3.8确认密码元素
    confirm_password=['xpath','//*[@id="confirmPwd"]']
    # 3.9确认按钮
    confirm = ['xpath', '//*[@id="submitBtn"]']
p=Page_elem()



















