#coding=utf-8
"""
Author:多测师_李立伏
time:2022-02-08 10:32
Wechat:xiaoshubass
website:www.duoceshi.cn
"""
from public.pages.basepages import Basepages
from selenium import webdriver
from time  import sleep
from public.utils.read_ini import read
import unittest
from public.pages.page_element import p
class Adduser(Basepages):
    @classmethod
    def setUpClass(cls) -> None:
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        pass
    def test_01user_control(self):
        user_control=["xpath",'//*[@id="menu-user"]/dd/ul/li[1]/a']
        elem=Basepages.find_element(user_control)
        Basepages.click(elem)
    def test_02adduser(self):
        elem=["xpath",'//*[@id="iframe_box"]/div[2]/iframe']
        iframe=Basepages.find_element(elem)
        Basepages.switch_iframe(iframe)
        elem1=Basepages.find_element(p.adduser)
        Basepages.click(elem1)
        elem2=['xpath','//*[@id="xubox_iframe1"]']
        iframe1=Basepages.find_element(elem2)
        Basepages.switch_iframe(iframe1)
        elem3=Basepages.find_element(p.adduseranme)
        Basepages.sendkeys(elem3,'llf')
        elem4=Basepages.find_element(p.sex)
        Basepages.click(elem4)
        elem5=Basepages.find_element(p.cellphone)
        Basepages.sendkeys(elem5,'18375684719')
        elem6=Basepages.find_element(p.mailbox)
        Basepages.sendkeys(elem6,'867985436@qq.com')
        elem7=Basepages.find_element(p.id)
        Basepages.sendkeys(elem7,'root')
        elem8=Basepages.find_element(p.password)
        Basepages.sendkeys(elem8,'123456')
        elem9=Basepages.find_element(p.confirm_password)
        Basepages.sendkeys(elem9,'123456')
        elem10=Basepages.find_element(p.confirm)
        Basepages.click(elem10)



