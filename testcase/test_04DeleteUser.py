#coding=utf-8
"""
Author:多测师_李立伏
time:2022-02-08 14:26
Wechat:xiaoshubass
website:www.duoceshi.cn
"""
from public.pages.basepages import Basepages
from selenium import webdriver
from time  import sleep
from public.utils.read_ini import read
import unittest
from public.pages.page_element import p
class Deleteuser(Basepages):
    @classmethod
    def setUpClass(cls) -> None:
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        pass
    def test_01deleteuesr(self):
        Basepages.switch_default()
        iframe=['xpath','//*[@id="iframe_box"]/div[2]/iframe']
        elme=Basepages.find_element(iframe)
        Basepages.switch_iframe(elme)
        sleep(1)
        checkbox=['xpath','//*[@id="sysUserTab"]/tr[1]/td[1]/input']
        elme1=Basepages.find_element(checkbox)
        Basepages.click(elme1)
        delete=['xpath','/html/body/div/div[2]/span[1]/a[1]']
        elme2=Basepages.find_element(delete)
        Basepages.click(elme2)
        sleep(1)
        confirm=['xpath','//*[@id="xubox_layer1"]/div[1]/span[2]/a[1]']
        elme3=Basepages.find_element(confirm)
        Basepages.click(elme3)

