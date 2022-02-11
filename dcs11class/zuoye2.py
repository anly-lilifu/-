#coding=utf-8
"""
Author:多测师_李立伏
time:2022-01-19 17:46
Wechat:xiaoshubass
website:www.duoceshi.cn
"""
# 12、分析以下数字的规律， 1 1 2 3 5 8 13 21 34用Python语言编程实现输出
# def func(n):
#     list1=[]
#     for i in range(n):
#         if i==0 or i==1:
#             list1.append(1)
#         else:
#             list1.append(list1[-1]+list1[-2])
#     print(list1)
# func(9)

# # 16、用递归的方法求出n的阶乘？4的阶乘结果为?
# def func(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*func(n-1)
# print(func(5))



# 3、用for循环打印九九乘法表
# def func():
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print(i,"*",j,"=",i*j,end=" ")
#         print("")
# func()
# 15、水仙花数：一个三位数，其按位立方之和等于该数本身，该数称为水仙花数。求出100 - 1000之间的水仙花数。
# 其实，水仙花数是“自幂数”中的一种；自幂数：一个n位数，其按位数字的n次方之和，等于该数本身。
# def func():
#     for i in range(100,1000):
#         j=str(i)
#         a=int(j[0])
#         b=int(j[1])
#         c=int(j[2])
#         if a**3+b**3+c**3==i:
#             print(i)
# func()

#  23、使用正则完成市面上手机规则的编写、随机生成11位数然后通过正则匹配出
# 符合规则的11位数手机号码？（手机号：11位）

# def func():
#     import string
#     import re
#     import random
#     num=string.digits
#     list1=[]
#     for i in range(11):
#         list1.append(random.choice(num))
#         c="".join(list1)
#     # print(c)
#     str1=re.findall("^1[3-9][0-9]\d{8}$",c)
#     if len(str1)==0:
#         func()
#     else:
#         print(str1[0])
# func()


# 10、冒泡排序,给一组无规律的数据从大到小或从小到大进行排序如：list = [2, 6, 9, 10, 18, 15, 1]
# def func():
#     list = [2, 6, 9, 10, 18, 15, 1]
#     for i in range(0,len(list)):
#         for j in  range(i+1,len(list)):
#             if list[i]>list[j]:
#                 list[i],list[j]=list[j],list[i]
#     print(list)
# func()

# 8、请写一段Python代码用for循环实现对list = [1, 3, 6, 9, 1, 8]里面的元素进行去重
# def func():
#     list1 = [1, 3, 6, 9, 1, 8]
#     list2=[]
#     for i in list1:
#         if i not in list2:
#             list2.append(i)
#         else:
#             continue
#     print(list2)
# func()
# 14、用字符串aabbcdbaaabc，用你熟悉的语言实现去除"ab"子串
def func():
    str1="aabbcdbaaabc"
    while "ab" in str1:
        str1=str1.replace("ab","")
    print(str1)
func()