#coding=utf-8
"""
Author:多测师_李立伏
time:2022-01-11 9:36
Wechat:xiaoshubass
website:www.duoceshi.cn
"""
#print ("多测师")   #python中的输出函数
'''
print ("多测师")
name="多测师"   #一个等号代表赋值
print(name)
'''


#print("python中的注释")
# 代表单行注释

#%s 格式化输入字符串
#name="中国"
#print ("%s 是 世界 第一"%name)

#%c：单个字符
#num="1"
#print("小明的英语成绩是%c分"%num)

#%d：十进制整数
#num=10
#print ("小明的成绩是%d分"%num)

# name=input("请输入您的账户:")
# print (type(name))
# if name=="admin":
#    print("欢迎vip客户")
# else:
#    print ("欢迎普通用户上线")

# money=int(input("请输入你需要取钱的金额:"))
# if money<100:
#     print("请输入正确的取款金额")
# elif money<10000 and money>=100:
#     print ("取钱成功")

a=5
b=3
#1
# a+=b #意思就是a=a+b
# print (a)
# 2
# a-=b #意思就是a=a-b
# print (a)
#3
# a*=b #意思就是a=a*b
# print (a)
#4
# a/=b  #意思就是a=a/b
# print (a)
#5
# a**=b  #意思就是a=a的b次方
# print (a)
#6
# a//=b   #意思就是a=a/b的商数
# print (a)
#7
# a%=b   #意思就是a=a/b的余数
# print (a)


#python的比较运算符
# a=5
# b=3
# print (a>b)     #True   #比较后会返回布尔值：判定真假（TRUE(真）  FALSE(假））
# print (a<b)     #False
# print (a<=b)    #False   此时的<和= 是或的关系
# print (a>=b)    #True   此时的<和= 是或的关系
# print (a>b and b<=a)   #True
# print (a>b or b>a)     #True
# print (a>b and b>a)   #False
# python中的成员运算符
# list1=[1,2,3,"4",5,6,"haha","xixi"]
# a=2
# b=1
# c=4
# d="haha"
# print (c in list1) #c=4 而列表中的“4”为sit格式，不是int格式。所以为错
# print (b in list1) #True
# print (b not in list1) #False #b not in list1:b不在list1这个列表中

# python中的按位运算符 #计算机中为2进制，最底层为8位字符
# 0    0   0   0   0   0   0   0
#128  64  32  16   8   4   2   1
# a=10
# 00001010
# b=20
# 00010100
#&：按位与运算==》当转换为2进制数时，同位置的值都为1时则取1
# print (a&b)

#|：按位或： ==》当转换为2进制数时，同位置的值有一个1时就取1
# print (a|b)

#^按位异或：当转换为2进制数时，同位置的值不相同时就取1
# print (a^b)

#按位取反：-（x+1）
# print (~-10)

#向左移动 在二进制位数右边添加两个0
# print (a<<2)
# a=10
# 00001010
# 00101000
#向右移动 在二进制位数左边添加两个0
# print (a>>2)
# a=10
# 00001010
# 00000010

# 切片索引
# strl="abcdefghjkl"
# print (strl[0:4]) #abc
# print (strl[4:7]) #efg
# print (strl[3:]) #defghjkl
# print (strl[0:]) #abcdefghjkl
# print (strl[0:8:2]) #aceg
# print (strl[2:4:-1])#空值
# print (strl[-2:-6:-1])  #kjhg
# print (strl[3:-2:-1]) #空值
# print (strl[:-2:1])  #abcdefghj
# print (strl[::])  #abcdefghjkl
# print (strl[::-1])   #lkjhgfedcba

# print (strl[-3::-1]) #jhgfedcba
# print (strl[-3::1]) #jkl

# #python中操作字符串的函数
# str2="user_name"
# # capitalize函数：将字符串的首字母变为大写
# print (str2.capitalize())   #User_name
# #title函数：将字符串中只要出现第一个开头是字母的就会将此字母变为大写
# print (str2.title())    #User_Name
# #split函数：通过什么将字符串进行分割，加入到一个列表当中
# print (str2.split("n"))
# #join函数：通过某个字符将字符串进行连接
# # print ("*".join(str2))
# #count()函数：可以用来统计字符串中元素出现的次数
# # print (str2.count("e"))   #2
# #startswith():判断字符串以什么开头
# print (str2.startswith("u"))   #True
# # #endswith()：判断字符串以什么结尾
# # print (str2.endswith("t"))   #False

 # 1 2 3 4 5 6 7 10 11 12 13 14
num=12
print("china is number %o"%num)

num=17
print("china  is number %x"%num)


num=12
print("china  is number %x"%num)

_list=(1,2,3,4,5,6,6,)
print(_list)






































































































