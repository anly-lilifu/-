#coding=utf-8
"""
Author:多测师_李立伏
time:2022-01-12 9:07
Wechat:xiaoshubass
website:www.duoceshi.cn
"""
# 第一列表的第一种方式：
# list1=[1,2,3,4,"hello","12314",["成都","四川","nihao"]]
# print (list1[-1])      # ['成都', '四川', 'nihao']
#第二种定义列表的方式
# str1="qawdads"
# list2=list(str1)
# # print(list2)
#列表中的赋值
# list3=[1,2,3,4,"hello","12314",["成都","四川","nihao"]]
# list3[3]="李四"
# print(list3)
# list3[-1][0]="达州"
# print(list3)

# 类似于赋值的方法，不仅可以替换掉需要替换的片段，还可以将多出来的元素插入进入被替换的这个列表。
# list3=[1,2,3,4,"hello","12314",["成都","四川","nihao"]]
# list3[3:6]=list('12345677')  将list1中的元素插入到“list3中[3:6]这个索引位中”
# print(list3)
# 操作列表的函数
# 列表中的追加函数：append
# list1=[1,2,3,4,5,]
# str1="绵阳"
# print(list1.append(str1))   这个是打印追加元素的这个动作
# print(list1)

# 列表连接函数：extend()
# list1=[1,2,3,4,5]
# list2=['1','2','2','3']
# list1.extend(list2)   #将list2中的内容追加到list1里面去
# print(list1)

#列表中的插入元素 insert（），指定位置进行插入元素
# list1=[1,2,3,4,"hello","中国"]
# list1.insert(1,"小王")     #指定在1号索引位插入一个“小王”
# print(list1)
# list1[0]="李四"         #将0号索引位的值换成“李四”
# print(list1)

#列表中的移除：remov（）函数，删除列表中的指定元素
# list1=[1,2,3,4,5,"小王","成都"]
# list1.remove("小王")  #一个删除list1列表中“小王”这个元素的过程。
# print(list1)
#查找列表中元素的索引位： index指定片段，进行查找元素的索引位（如果不指定片段就默认从左至右第一个）
# list1=[1,2,3,4,5,"小王","成都",2]
# print(list1.index("成都"))    #查找成都在list1这个列表中的索引位
# print(list1.index(2,-6)) #查找2这个元素在list1这个列表中-6位置之后的2这个元素的索引位（类似于切片）

# 对于列表进行排序：sort（函数）
# list2=["1","2","3","4","5",2]
# list2.sort()
# print(list2)  #不同类型的数据不能进行排序

# list3=["1","9","80","16",'zhangsan','lisi','张三','李四']  #比较字符串，需要通过ASC码进行比较
# list3.sort()
# print(list3)


# list1=[12,23,24,42,10,31,20]
# list1.sort()
# print(list1)
# #对于列表进行排序：sorted（）函数（reverse=TRUE 降序，revice=FALSE 升序）
# print(sorted(list1,reverse=True))
# print(sorted(list1,reverse=False))

#对于列表进行删除，pop（）函数，默认删除列表最后一个元素，并且返回删除的值
# list1=[12,23,24,42,10,31,20]
# print(list1.pop())  输出查看删除的过程，得到一个删除的元素  唯一一个可以查看删除过程的函数
# print(list1)       查看删除后剩余的元素
# print(list1.pop())  在上一次删除的前提上再次删除一个值
# print(list1)
#将列表进行反转：reverse（）函数  列表的排序进行反转(类似于将字符串的索引位反向输出）
# list1=[12,23,24,42,10,31,20]
# list1.reverse()
# print(list1)


# list1=[12,23,24,42,10,31,20]
# print(list1[::-1])  类似于将字符串的索引位反向输出

# del 关键字
# list1=[12,23,24,42,10,31,20]
# del list1[0]    #删除list1这个列表中索引位为0的元素
# print(list1)
#
# del list1  #直接删除list1这个列表

# python中的元组
# tuple1=(1,2,3,'nihao','haha',[4,5,"zaijian",'name'],('zhangsan','lisi'))
# print(tuple1)

# print(type(tuple1))
# tuple2=("wangwu",)
# print(type(tuple2))


#将元组转换成列表的方法：
# list1=list(tuple1)
# print(list1)

#将列表转为元组
# tuple2=tuple(list1)
# print(tuple2)
#改变元组中元组的方法：
# tuple1=(1,2,3,'nihao','haha',[4,5,"zaijian",'name'],('zhangsan','lisi'))
# print(tuple1[6])
# # tuple1[6][0]="多测师"   #报错，因为他是一个元组，不能被修改
# tuple1[5][0]="多测师"   #将tuple1中的5号索引位对应的元素中的第0位索引的值换成“多测师”
# print(tuple1)


# tuple1=(1,2,3,'nihao','haha',[4,5,"zaijian",'name'],('zhangsan','lisi'))
# list1=list(tuple1)
# print(list1)
# # # print(type(list1[-1]))
# # list2=list(list1[-1])
# # list1[-1]=list2
# list1[-1]=list(list1[-1])
# # print(list2)
# print(list1)

#第一种定义字典的方式：
# dict1={"name":"xiangwang","age":18,"score":[90,80,8]}
# print(dict1)
# print(type(dict1))

#第二种定义字典的方式：但是格式必须满足以下格式[["姓名","xiaowang"],["年龄",19]]
# list1=[["姓名",'小王'],['年龄',19]]
# dict1=dict(list1)
# print(dict1)
# print(type(dict1))

#字典中常见的赋值操作：
# dict1={'name':'xiaowang','age':18,'score':[90,28,80]}
# print(dict1['name'])
# dict1['score']=100    #因为字典是无序的，所以不能用索引，只能用键来取对应的值，但是括号还是要用[]
# print(dict1)
# dict1['class']=1833 #如果输入的这个键没有，则会新建一个键值对
# print(dict1)

# # 字典中用的方法
# 1.取出字典中所有的键：
# a遍历，for循环
# dict1={'name':'xiaowang','age':18,'score':100,'class':1833}
# # for i in dict1:    #取出字典中所有的键名
# #     print(i)
# #b取出字典中所有的键名
# print(dict1.keys())
#
# #2取出字典中所有的值
# # a：通过valus方法取值
# print(dict1.values())
# #b通过遍历进行取值 dict1[i]代表将遍历出来的键名带入待字典中进行取值
# for i in  dict1:
#     print(dict1[i])

#给字典设置键值对：
# dict1={'name':'xiaowang','age':18,'score':100,'class':1833}
# # dict1['haha']='张三'
# print(dict1)

#通过setdefault(）函数进行添加键值对：如果键名存在，那么设置无效
# dict1.setdefault('dcs','11ban')
# print(dict1)
# dict1.setdefault('dcs','12ban')


# dict1={'name':'xiaowang','age':18}
# #字典中删除并且返回的函数：pop函数
# # print(dict1.pop('name'))
# # print(dict1)
# #
# # #清楚字典中的所有键值对 ：clear（）
# # dict1.clear()
# # print(dict1)
# # #用函数取出字典中键对应的值： get（）函数
# print(dict1.get("name"))


#更新字典中的内容：updete()函数
# dict1={'name':'xiaowang'}
# dict2={'age':18}
# # dict1.update(dict2)
# print(dict1)
dict1={'name':'xiaowang','age':20}
dict2={'age':18}
dict1.update(dict2)#如果有相同的键，则会更新为新的的值
print(dict1)

#fromkeys函数：用来给所有的键附上一个相同的值
print({}.fromkeys(['name','age'],'xiaomig'))


#popitem()函数：删除键值对，并且返回删除的键值对















































