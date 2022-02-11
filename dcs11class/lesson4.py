#coding=utf-8
"""
Author:多测师_李立伏
time:2022-01-16 14:15
Wechat:xiaoshubass
website:www.duoceshi.cn
"""
# name=input("请输入你要查询的内容：")
# if name=="小王":
#     print("成都11班")
# else:
#     print("成都12班")

# name=input("请输入你要查询的值")
# print('成都11班')  if name=="小王"   else print("成都12班")

# # python中的格式化输出
# str1="{}已经{}".format("小王","18岁")
# print(str1)
#
# # 按照入参的索引位进行格式化输出
# str1="{0}{1}{1}{2}{2}{0}".format("多测师","成都","广州")
# print(str1)
#
# # 按照制定参数进行格式化输出：
# str1="姓名：{name} 年龄：{age}".format(name="小王",age="18岁")
# print(str1)

# list1=["小王",'18岁',"1832班"]
# str1="姓名{[0]} 年龄{0[1]} 班级{[0]}".format(list1)













# 存在一个文件, 文件名test.txt
# 内容如下：
# 01 success
# 02 fail
# 03 fail
# 04 success
# ....请使用Python语言编写程序实现统计该文件中
# 有多少个success
# 多少个fail的功能？
o=open(r"D:\duoceshi\dcs11class\test.txt","r",encoding="utf-8")
all=o.read()
print(type(all))
# dict1={}
# print(dict1)
print("success",all.count("success"))
print("fail",all.count("fail"))

# o=open(r"D:\duoceshi\dcs11class\test.txt","r",encoding="utf-8")
# x=o.readlines()
# sum1=0
# sum2=0
# for y in x:
#     if y.count('success')!=0:
#         sum1+=y.count('success')
#     elif y.count('fail')!=0:
#         sum2+=y.count('fail')
#     else:
#         pass
# print('有%d个success'%(sum1))
# print('有%d个fail'%(sum2))




# 19、一个txt文件中已知数据为：
# C4D
# C4D/maya
# C4D
# C4D/su
# C4D/max/AE
# 统计每个字段出现的次数，比如C4D,maya,su,max,AE 请用最熟悉的语言或者伪代码实现该需求
# o=open(r"D:\duoceshi\dcs11class\test1.txt","r",encoding="utf-8")
# all=o.readlines()
# list1=[]
# list2=[]
# list3=[]
# # print(all)
# for i in all:
#     if "\n" not in i:
#         list1.append(i)
#     else:
#         i=i.replace("\n","")
#         list1.append(i)
# for a in  list1:
#     if "/" in a:
#         # print(a)
#         list2.extend(a.split("/"))
#     else:
#         list2.append(a)
# # print(list1)
# # print(list2)
# for i in list2:
#     # print(l)
#     if i not in list3:
#         list3.append(i)
# # print(list3)
# dict={}
# for i in list3:
#     dict[i]=(list2.count(i))
# print(dict)




# 20、统计一个文件的行数，以e:\\write.txt文件为例(内容自己建)
# o=open(r"D:\duoceshi\dcs11class\ewrite..txt","r",encoding="utf-8")
# all=o.readlines()
# a=0
# for i in all:
#     if "\n" in i:
#         a=a+1
# print(a+1)
