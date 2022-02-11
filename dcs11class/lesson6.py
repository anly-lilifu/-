#coding=utf-8
"""
Author:多测师_李立伏
time:2022-01-20 10:40
Wechat:xiaoshubass
website:www.duoceshi.cn
"""
#
# class Li(object):
#     def __init__(self,name,age):
#         self.a=name
#         self.c=age
#     def instance_method(self):
#         print(self.a+"月入百万")
#
#     @classmethod
#     def class_methods(cls):
#         print("会说话")
#
#     @staticmethod
#     def static_method():
#         print("会吃饭")
#

class Gardfather(object):
    def dabce(self):
        print("喜欢下棋")
class Father(object):
    def drink(self):
        print("喜欢喝酒")
    def driver(self):
        print("喜欢开车")
    def rich(self):
        print("富有")
f=Father()
class Son(Father,Gardfather):
    def meinv(self):
        print("喜欢美女")
    def read(self):
        print("喜欢看书")
s=Son()
s.dabce()
s.drink()
s.meinv()
s.driver()
s.rich()