#coding=utf-8
"""
Author:多测师_李立伏
time:2022-01-14 9:03
Wechat:xiaoshubass
website:www.duoceshi.cn
"""

# 1、求出1 / 1 + 1 / 3 + 1 / 5??+1 / 99的和
# sum=0
# for i in  range(1,100,2):
#     sum=sum+1/i
# print(sum)

# 2、用循环语句，计算2 - 10之间整数的循环相乘的值。
# sum=1
# for i in range(2,10):
#     sum=sum*i
# print(sum)

# 3、用for循环打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"*",j,"=",i*j,end="   ")
#     print()


# 4、求每个字符串中字符出现的个数如：helloworld
# str1=("helloworld")
# dict1={}
# for i in str1:
#     # print(str1.count(i))
#     dict1[i]=str1.count(i)
# print(dict1)

# 5、实现把字符串str = "duoceshi"中任意字母变为大写、在输入函数中输入DCE输出结果为：DuoCEshi
# str1="duoceshi"
# name=input("请输入你输入需要改变的字母：")
# a=name.lower()
# for i in a:
#     j=i.upper()
#     str1=str1.replace(i,j)
# print(str1)

# 6、求出1900 - 2017年的闰年？
# 普通闰年:能被4整除但不能被100整除的年份为普通闰年。（如2004年就是闰年，1999年不是闰年）
# 世纪闰年:能被400整除的为世纪闰年。（如2000年是世纪闰年，1900年不是世纪闰年）
# list2=[]
# list1=[]
# for i in range(1900,2018):
#     if i%4==0 and i%100!=0:
#         list1.append(i)
#     elif i%400==0:
#         list2.append(i)
# print(list2)
# print(list1)

# 7、分别打印100以内的所有偶数和奇数并存入不同的列表当中
# list1=[]
# list2=[]
# for i in range(1,100,2):
#    list1.append(i)
# print(list1)
# for i in range(0,101,2):
#     list2.append(i)
# print(list2)


# 8、请写一段Python代码用for循环实现对list = [1, 3, 6, 9, 1, 8]里面的元素进行去重
# list1=[1, 3, 6, 9, 1, 8]
# list2=[]
# def func():
#     for i in list1:
#         if i not in list2:
#             list2.append(i)
#         else:
#             pass
#     print(list2)
# func()

# 9、利用for循环把字符串user_controller转换为驼峰命名UserController
# def func():
#     str1 = "user_controller"
#     str2 = ''
#     str3 = ''
#     str2=str1.title()
#     # print(str2)
#     for i in str2:
#         if i=="_":
#             continue
#         str3=str3+i
#     print(str3)
# func()

# 10、冒泡排序,给一组无规律的数据从大到小或从小到大进行排序如：list = [2, 6, 9, 10, 18, 15, 1]
# def func():
#     list1 =[2, 6, 9, 10, 18, 15, 1]
#     # print(len(list1))
#     for i in range(0,len(list1)):
#         for j in range(i+1,len(list1)):
#             if list1[i]>list1[j]:
#                 list1[i],list1[j]=list1[j],list1[i]
#     print(list1)
# func()
# 12、分析以下数字的规律， 1 1 2 3 5 8 13 21 34用Python语言编程实现输出
# def func(n):
#     list1=[]
#     for i in  range(n):
#         if i==0 or i==1:
#             list1.append(1)
#         else:
#             list1.append(list1[-1]+list1[-2])
#     print(list1)
# func(8)


# 13、先定义一个字典来存放用户名
# 和密码如dic = {'admin': '123456', 'dcs46': '654321'}
# 要求如下：
# 1）、从字典中获取用户完成登入，登入时判断用户是否存在
# 存在直接登入
# 2）、如果输入的登入用户判断不存在字典，则调用注册方法，完成该用户的注册，注册成功后写入字典
# 定义登录函数
# dict1 = {'admin': '123456', 'dcs46': '654321'}
# def denglu():
#     a=input("输入用户名：")
#     if dict1.__contains__(a):
#         b=input("请输入密码")
#         if b==dict1[a]:
#             print("登录成功")
#         else:
#             print("登录失败")
#     else:
#         print("你还未进行注册，请先进行注册")
#         c=input("请输入注册的密码：")
#         dict1.setdefault(a,c)
#         print('注册成功')
#         print(dict1)
# denglu()


# 14、用字符串aabbcdbaaabc，用你熟悉的语言实现去除"ab"子串
# str1="aabbcdbaaabc"
# while 'ab' in str1:
#     str1=str1.replace('ab','')
# print(str1)



# 15、水仙花数：一个三位数，其按位立方之和等于该数本身，该数称为水仙花数。求出100 - 1000之间的水仙花数。
# 其实，水仙花数是“自幂数”中的一种；自幂数：一个n位数，其按位数字的n次方之和，等于该数本身。
# for i in range(100,1000):
#     str1=str(i)
#     # print(str1)
#     a=int(str1[0])
#     b=int(str1[1])
#     c=int(str1[2])
#     if a**3+b**3+c**3==i:
#         print(i)








# 16、用递归的方法求出n的阶乘？4的阶乘结果为?
# def a(i):
#     if i==1:
#         return 1
#     else:
#         y=i*a(i-1)
#         return y
#
# print(a(4))
#
#
# def func1(n):
#     if n==1:
#         return 1
#     else:
#         x=n*func1(n-1)
#         return x
# print(func1(4))



# 17、有如下url地址, 要求实现截取出"?"号后面的参数, 并将参数以"key value"的键值形式保存起来, 并最终通过#get(key)的方式取出对应的value值。
# url地址如下：
# # http://ip:port/extername/get_account_trade_record.json?page_size=20&page_index=1&user_id=203317&trade_type=0"
# str1="http://ip:port/extername/get_account_trade_record.json?page_size=20&page_index=1&user_id=203317&trade_type=0"
# list1=str1.split("?")
# list2=list1[1].split("&")
# dict1={}
# # print(list2)
# for i in list2:
#     # print(i)
#     list3=i.split("=")
#     dict1.setdefault(list3[0],list3[1])
# print(dict1)
# # def get(key):
# #     print()
# # get(key)
#
# list1=[1,2,3,4,5,6,"7","hello","china"]
# print(list1[:7])
# print(list1[-2][-1])

# 18、存在一个文件, 文件名test.txt
# 内容如下：
# 01 success
# 02 fail
# 03 fail
# 04 success
# ....请使用Python语言编写程序实现统计该文件中
# 有多少个success
# 多少个fail的功能？


# 19、一个txt文件中已知数据为：
# C4D
# C4D/maya
# C4D
# C4D/su
# C4D/max/AE
# 统计每个字段出现的次数，比如C4D,maya,su,max,AE 请用最熟悉的语言或者伪代码实现该需求


# 20、统计一个文件的行数，以e:\\write.txt文件为例(内容自己建)
# def func(path):
#     num_count=1
#     o=open(path,'r',encoding="utf-8")
#     all=o.readlines()
#     for i in all:
#         if "\n" in i:
#             num_count+=1
#         else:
#             continue
#     print(num_count+1)
# func(r"D:\duoceshi\dcs11class\test1.txt")



# 21、使用os模块写一个递归调用打印出e:\\home下的所有文件名的绝对路径？
# import os
# def get_path (path) :
#     a=os. listdir(path) # 列出传入路径 下的所有目录和文件
#     # print (a)
#     for i in a:		#遍历列出的文件
#         # print(i)
#         newpath=os. path. join(path, i) 	#使用传入的path和文件进 行拼接成绝对路径
#     # print (newpath)
#         if os. path. isdir (newpath) :	#通过绝对路径进行判断是否是一 个目录。 如果是一 个目录， 那么就调用自己
#             get_path (newpath)
#         else:
#             print (newpath)	#如果是文件，那么就打印拼接后的结果
# get_path("D: \home" )

# 22、用正则方法实现统计e:\\python文件中指定字符如"python"的行数?（文件中的python字符）假设里面的数据为：
# pythonelloerror
# warnipythonngerror
# warning
# errorwapythonrning

# import re
# def get_py_rows (path):
#     o=open (path,"r")
#     all=o. readlines()
#     num=0
#     # print(all)
#     for i in all:
#         # print(i)
#         str1=re.findall('python',i)
#         print (str1)
# #第一“种:
#         if "python" in strl:
#             num+=1
# #第二种:
#         if len(str1)!=0:
#             num+=1
#     print (num)
# get_py_rows (r"C: \Users\1 iujian\PycharmProjects\dcs11\lesson\test. txt")

# 23、使用正则完成市面上手机规则的编写、随机生成11位数然后通过正则匹配出
# 符合规则的11位数手机号码？（手机号：11位）
import random
import string
import re
# 第一种:
def get_phone () :
    num=string.digits	#生成0 ^9的数字
    list1=[]
    for i in range(11):	#遍历11此，每遍历 一次就选取一个添加到listI中
        list1.append(random.choice(num))
        phone="".join(list1)    #拼接1istI中的元素
# print (phone)
    str1=re.findall("^1[3-9][0-9]\d{8}$",phone) #用 正则匹配取四配出符合规则的手机号。有可能匹配为空
    if len(str1)==0: 	#如果匹配为空就再次调用自己
        get_phone ()
    else:	#如果不为空就打印匹配出来的内容
            print (str1[0])
get_phone ()
# #第二种:
# def get_phone() :
#     str1=[]
#     while len(str1)==0:		#使strI长度为0时进入循环
#         num=string. digits
#         list1=[]
#         for i in range(11):
#             list1. append (random. choice (num) )
#             phone="". join(list1)
#             # print (phone)
# #匹配出符合规则的内容。有可能为空那么 长度就为0会重复进行循环
# #知道长度大F0那么就跳出循环，打印str1中索 引位为0的元素
#             str1=re. findall("1[3^ °9] [0~9] \d{8} $", phone)
#         print (str1[0])
# get_phone ()


# 24、用正则实现写一段代码统计e:\\log文件中error和warning单词出现的次数分别为几次?
# 文件内容如下：
# warningabchelloerrorwarningwarning
# warningerror
# warning
# errorwarningwarning

# def func (path) :
#     dict1={}
#     o=open(path,'r' )
#     al1=o.read()
#     # print(a1l)
#     str1=re.findall('warning', al1)
#     # print(strI)
#     str2=re. finda1l('error', a1l)
# # print (str2)
# #第一种:
#     print('文件中waring出现的次数是%d' %len(str1))
#     print('文件中error出现的次数是%d' %len(str2))
# #第二种:
#     for i in strl:
#         if i not in dict1. keys():
#             dictl. setdefault(i,1)
#         else:
#             dict1[i]=dict1[i]+1.
#     for j in str2:
#         dict1[j]=1 if j not in dict1.keys() else dict1[j]+1
#         print (dict1)
# func (r"C: \Users\liujian\PycharmProjects\dcs11\lesson\成都多测师")