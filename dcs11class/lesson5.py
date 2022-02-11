#coding=utf-8
"""
Author:多测师_李立伏
time:2022-01-17 14:06
Wechat:xiaoshubass
website:www.duoceshi.cn
"""
# import time
# print(time.time())
# print(time.ctime())
# print(time.sleep(2))
# print(time.asctime())
# print(time.strftime("%Y"))


# from time import ctime
# print(ctime())
# from time import time
# print(time())

# from time import *
# print(ctime(),time())

# from time import time as a
# print(a())

# from dcs13.haha import a
# a()
# 1、使用random模块随机生成手机号码、自己定义手机号码开头的前三位
# def a():
#     list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     str1=()
#     import random
#     b=(random.sample(list1,8))
#     if len(b)<9:
#         b.insert(0,3)
#         if len(b)<10:
#             b.insert(0,8)
#             if len(b)<11:
#                 b.insert(0,1)
#     for i in b:
#         print(i,end="")
# a()


# 2、用random模块随机生成6位数验证码
#
# def a():
#     import string
#     str1=string.digits+string.ascii_letters
#     list2=[]
#     # print(list1)
#     c=""
#     import random
#     # print(random.choice(list1))
#     for i in range(6):
#         a=random.choice(str1)
#         list2.append(a)
#     str2="".join(list2)
#     return (str2)
# a()
#
# # 3、通过md5加密算法把随机生成的6位数验证码进行加密返回16进制的字 符串
# def c():
#     import hashlib
#     # print(d)
#     md5=hashlib.md5()
#     md5.update(a().encode("utf-8"))
#     print(md5.hexdigest())
# c()


# 21、使用os模块写一个递归调用打印出e:\\home下的所有文件名的绝对路径？
# list2=[]
# list1=[]
# def func(path):
#     import os
#     list1=(os.listdir(path))
#     # print(len(list1))
#     for i in list1:
#         a=os.path.join(path,i)
#         if os.path.isfile(a):
#             list2.append(a)
#         else:
#             func(a)
#     # print(list2)
#     # print(len(list2))
# func(r"D:\Python37")
# print(list2)
# print(len(list2))


# def func(path):
#     import os
#     list1=(os.listdir(path))
#     # print(len(list1))
#     for i in list1:
#         a=os.path.join(path,i)
#         if os.path.isfile(a):
#             print(a)
#         else:
#             func(a)
# func(r"D:\Python37")
#





# 22、用正则方法实现统计e:\\python文件中指定字符如"python"的行数?（文件中的python字符）
# 假设里面的数据为：
# pythonelloerror
# warnipythonngerror
# warning
# errorwapythonrning
# def func(path):
#     o=open(path,"r",encoding="utf-8")
#     all=o.readlines()
#     num=0
#     import re
#     for i in all:
#         str1=re.findall("python",i)
#         # print(str1)
#         if "python" in str1:
#             num+=1
#     print(num)
# func(r"D:\duoceshi\dcs13\python.txt")







# 23、使用正则完成市面上手机规则的编写、随机生成11位数然后通过正则匹配出
# 符合规则的11位数手机号码？（手机号：11位）
import string
str1=string.digits
print(str1)





# 24、用正则实现写一段代码统计e:\\log文件中error和warning单词出现的次数分别为几次?
# 文件内容如下：
# warningabchelloerrorwarningwarning
# warningerror
# warning
# errorwarningwarning