#coding=utf-8
"""
Author:多测师_李立伏
time:2022-01-29 12:40
Wechat:xiaoshubass
website:www.duoceshi.cn
"""
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get("http://www.bilibili.com")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="i_cecream"]/div[1]/div[1]/ul[2]/li[1]/li/div/div').click()
sleep(2)
handle=driver.current_window_handle
handle1=driver.window_handles
driver.switch_to.window(handle1[-1])
sleep(2)
# for i in handle1:
#     if i !=handle:
#         driver.switch_to.window(i)
# print(driver.title)
driver.find_element_by_xpath('//*[@id="login-username"]').send_keys("18375684719")
driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys("lili5573182555")
driver.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()
sleep(8)