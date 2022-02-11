#coding=utf-8
"""
Author:多测师_李立伏
time:2022-01-15 9:05
Wechat:xiaoshubass
website:www.duoceshi.cn
"""
# def a():
#     print("欢迎来到四川")
# a()

# def a(where):
#     print("欢迎"+where)
# a("你")
#
# def a(b,c):
#     print(b+c)
# a("中国","四川")
#
# def a(b,c):
#     print(b+c+"欢迎你")
# a("中国","四川")

# def a(action,where="四川"):
#     print(action+"的"+where)
# a("中国")
#
# def a(action,where="四川"):
#     print(action+"的"+where)
# a("中国","达州")
#
# def a(*b):
#     for i in b:
#         print(i)
# a("李四","王五")
#
# dict1={"name":"李四","age":17}
# def a(**dict):
#     print(dict)
# a(**dict1)


# 需求：
# 登录银行系统并显示余额，有两个功能第一个是登录，
# 第二个是登录后显示余额，先登录然后根据登录是否成功然后是否显示余额。
# 分析思路：如果想查询到余额，前提必须登录，所以现在我们用两个函数来 处理，
# 第一个函数实现登录，第二个函数实现余额查询，调用第一个函数得 到的结果给第二个函数，
# 然后第二个函数根据结果进行代码处理。
dict1={'admin':'123456',"zhangsan":"654321","lisi":"67890"}
dict2={'admin':4000,"zhangsan":3000,"lisi":800}

def a():
    user=input("请输入你的账户：")
    if dict1.__contains__(user):
        password=input("请输入你的密码：")
        if password==dict1[user]:
            print("登录成功")
            return ("登录成功",user)
        else:
            return ("密码错误，请重新输入密码",user)
    else:
        print("您输入的账户有误，请重新输入",user)

def b():
    denglu=a()
    if denglu[0]==("登录成功"):
       return (dict2[denglu[1]],denglu[1])



def c():
    money=b()
    qukuan=int(input("请输入你要取款的金额:"))
    if qukuan>money[0]:
        print("余额不足")
    elif qukuan<=money[0]:
        print("取款成功")
        dict2[money[1]]=money[0]-qukuan
        print(dict2)
    elif qukuan<0:
        print("余额不足")
c()




# 新增需求：
# 需要输入取钱的金额，并且判断取钱金额不能大于账户对应余额。
# 并且取完钱之后将剩余的余额在dict2中进行更新。

# 12、分析以下数字的规律， 1 1 2 3 5 8 13 21 34用Python语言编程实现输出
# a=0
# b=1
# i=0
# while i<9:
#     c=a+b
#     i=i+1
#     a=b
#     b=c
#     c=a
#     print(c)

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
# for i in range(100,1000):
#     str1=str(i)
#     # print(str1)
#     a=int(str1[0])
#     b=int(str1[1])
#     c=int(str1[2])
#     if a**3+b**3+c**3==i:
#         print(i)







# 其实，水仙花数是“自幂数”中的一种；自幂数：一个n位数，其按位数字的n次方之和，等于该数本身。
# 16、用递归的方法求出n的阶乘？4的阶乘结果为?
# def a(i):
#     if i==1:
#         return 1
#     else:
#         y=i*a(i-1)
#         return y
#
# print(a(4))




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








