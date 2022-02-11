#coding=utf-8
"""
Author:多测师_李立伏
time:2022-01-22 16:08
Wechat:xiaoshubass
website:www.duoceshi.cn
"""
# (1).登录

from selenium import webdriver
from time import sleep

# driver=webdriver.Chrome()
# driver.get("http://192.168.93.128/bbs")
# driver.maximize_window()
# driver.implicitly_wait(2)
# driver.find_element_by_id('ls_username').send_keys('admin')
# driver.find_element_by_id('ls_password').send_keys('123456')
# sleep(1)
# driver.find_element_by_xpath("//*[@type='submit']/em[1]").click()
# sleep(1)
# # driver.find_element_by_xpath("//*[@name='loginsubmit']/strong[1]").click()   #输入登录验证时的确认按钮
# # # 2.发帖
# driver.find_element_by_link_text("默认版块").click()
# sleep(2)
# js="window.scrollTo(0,1000)"
# driver.execute_script(js)
# sleep(1)
# driver.find_element_by_id("subject").send_keys("欢迎来到德莱联盟！！！")
# sleep(2)
# driver.find_element_by_name('message').send_keys("诺克萨斯即将崛起！！")
# sleep(2)
# driver.find_element_by_id("fastpostsubmit").click()
# sleep(1)
# # 3、回复帖子
# driver.find_element_by_class_name('fastre').click()
# driver.find_element_by_xpath("//*[@id='postmessage']").send_keys("哈哈")
# js="window.scrollTo(0,1000)"
# driver.execute_script(js)
# driver.find_element_by_xpath("//*[@id='postsubmit']/span").click()
# driver.find_element_by_xpath('//*[@id="mn_forum"]/a').click()
#
# # i+=1
# # driver.back()
# # sleep(5)
# # driver.quit()
#
#
# # 4.删帖：
# driver.find_element_by_link_text("默认版块").click()
# sleep(1)
# driver.find_element_by_link_text("欢迎来到德莱联盟！！！").click()
# driver.implicitly_wait(3)
# driver.find_element_by_link_text("删除主题").click()
# driver.implicitly_wait(3)
# driver.find_element_by_name("modsubmit").click()
#
# # # 5.管理删除提示
# sleep(1)
# from selenium.webdriver.common.action_chains import ActionChains
# mouse=driver.find_element_by_id("myprompt")
# sleep(1)
# ActionChains(driver).move_to_element(mouse).perform()
# driver.find_element_by_xpath('//*[@id="myprompt_menu"]/li[3]/a').click()
# sleep(1)
# driver.find_element_by_link_text("现在处理").click()
# sleep(2)
# # driver.find_element_by_name("admin_password").send_keys("123456")
# # sleep(2)
# # driver.find_element_by_xpath("//*[@id='loginform']/p[9]/input").click()
# # driver.implicitly_wait(3)
# driver.switch_to.frame(0)
# driver.find_element_by_xpath('//*[@class="td25"]/input[1]').click()
# sleep(1)
# js="window.scrollTo(0,500)"
# driver.execute_script(js)
# driver.find_element_by_name("delsubmit").click()
# sleep(3)








# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# class Cms(object):
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://192.168.93.128/bbs")
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(2)
#     def register(self):
#         self.driver.find_element_by_id('ls_username').send_keys('admin')
#         self.driver.find_element_by_id('ls_password').send_keys('123456')
#         sleep(1)
#         self.driver.find_element_by_xpath("//*[@type='submit']/em[1]").click()
#         sleep(1)
#     def post_a_message(self):
#         self.driver.find_element_by_link_text("默认版块").click()
#         sleep(2)
#         js="window.scrollTo(0,500)"
#         self.driver.execute_script(js)
#         sleep(3)
#         self.driver.find_element_by_id("subject").send_keys("欢迎来到德莱联盟！！！")
#         sleep(3)
#         self.driver.find_element_by_name('message').send_keys("诺克萨斯即将崛起！！")
#         sleep(5)
#         self.driver.find_element_by_id("fastpostsubmit").click()
#         sleep(5)
#         # driver.quit()
#     def shantie(self):
#         sleep(1)
#         self.driver.find_element_by_link_text("欢迎来到德莱联盟！！！").click()
#         self.driver.implicitly_wait(3)
#         self.driver.find_element_by_link_text("删除主题").click()
#         self.driver.implicitly_wait(3)
#         self.driver.find_element_by_name("modsubmit").click()
#     def Management(self):
#         sleep(1)
#         mouse=self.driver.find_element_by_id("myprompt")
#         sleep(1)
#         ActionChains(self.driver).move_to_element(mouse).perform()
#         self.driver.find_element_by_xpath('//*[@id="myprompt_menu"]/li[3]/a').click()
#         sleep(1)
#         self.driver.find_element_by_link_text("现在处理").click()
#         sleep(2)
#         # self.driver.find_element_by_name("admin_password").send_keys("123456")
#         # sleep(1)
#         # self.driver.find_element_by_name("submit")
#         # sleep(2)
#         self.driver.implicitly_wait(3)
#         sleep(2)
#         self.driver.switch_to.frame(0)
#         self.driver.find_element_by_xpath('//*[@class="td25"]/input[1]').click()
#         sleep(1)
#         js = "window.scrollTo(0,500)"
#         self.driver.execute_script(js)
#         self.driver.find_element_by_name("delsubmit").click()
# a=Cms()
# a.register()
# a.post_a_message()
# a.shantie()
# a.Management()

# from selenium import webdriver
# from time  import sleep
# driver=webdriver.Chrome()
# driver.get("http://192.168.93.128/bbs")
# driver.maximize_window()
# driver.find_element_by_name("username").send_keys("admin")
# driver.find_element_by_name("password").send_keys("123456")
# sleep(3)
# driver.find_element_by_xpath('//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button').click()
# sleep(5)
# driver.find_element_by_xpath('//*[@id="category_1"]/table/tbody/tr[1]/td[2]/h2/a').click()
# sleep(3)
# driver.find_element_by_link_text("欢迎来到德莱联盟！！！").click()
# sleep(3)
# driver.find_element_by_link_text("删除主题").click()
# sleep(3)
# driver.find_element_by_id("modsubmit").click()
# print("删除成功")

import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
# class Cms(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.driver = webdriver.Chrome()
#         cls.driver.get("http://192.168.93.128/bbs")
#         cls.driver.maximize_window()
#         cls.driver.implicitly_wait(2)
#     def test_001register(self):
#         self.driver.find_element_by_id('ls_username').send_keys('admin')
#         self.driver.find_element_by_id('ls_password').send_keys('123456')
#         sleep(1)
#         self.driver.find_element_by_xpath("//*[@type='submit']/em[1]").click()
#         sleep(1)
#     def test_002post_a_message(self):
#         self.driver.find_element_by_link_text("默认版块").click()
#         sleep(2)
#         js="window.scrollTo(0,500)"
#         self.driver.execute_script(js)
#         sleep(3)
#         self.driver.find_element_by_id("subject").send_keys("欢迎来到德莱联盟！！！")
#         sleep(3)
#         self.driver.find_element_by_name('message').send_keys("诺克萨斯即将崛起！！")
#         sleep(5)
#         self.driver.find_element_by_id("fastpostsubmit").click()
#         sleep(5)
#     def test_003shantie(self):
#         sleep(1)
#         self.driver.find_element_by_link_text("欢迎来到德莱联盟！！！").click()
#         self.driver.implicitly_wait(3)
#         self.driver.find_element_by_link_text("删除主题").click()
#         self.driver.implicitly_wait(3)
#         self.driver.find_element_by_name("modsubmit").click()
#     def test_004Management(self):
#         sleep(1)
#         mouse=self.driver.find_element_by_id("myprompt")
#         sleep(1)
#         ActionChains(self.driver).move_to_element(mouse).perform()
#         self.driver.find_element_by_xpath('//*[@id="myprompt_menu"]/li[3]/a').click()
#         sleep(1)
#         self.driver.find_element_by_link_text("现在处理").click()
#         sleep(2)
#         # self.driver.find_element_by_name("admin_password").send_keys("123456")
#         # sleep(1)
#         # self.driver.find_element_by_name("submit").click()
#         # sleep(2)
#         self.driver.implicitly_wait(3)
#         sleep(2)
#         self.driver.switch_to.frame(0)
#         self.driver.find_element_by_xpath('//*[@class="td25"]/input[1]').click()
#         sleep(1)
#         js = "window.scrollTo(0,500)"
#         self.driver.execute_script(js)
#         self.driver.find_element_by_name("delsubmit").click()
#     @classmethod
#     def tearDownClass(cls) -> None:
#         cls.driver.quit()
# if __name__ == '__main__':
#     unittest.main()

# class Cms(unittest.TestCase):
#     def setUp(self) -> None:
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://192.168.93.128/bbs")
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(2)
#     def test_001register(self):
#         self.driver.find_element_by_id('ls_username').send_keys('admin')
#         self.driver.find_element_by_id('ls_password').send_keys('123456')
#         sleep(1)
#         self.driver.find_element_by_xpath("//*[@type='submit']/em[1]").click()
#         sleep(1)
#     def test_002post_a_message(self):
#         self.test_001register()
#         self.driver.find_element_by_link_text("默认版块").click()
#         sleep(2)
#         js="window.scrollTo(0,500)"
#         self.driver.execute_script(js)
#         sleep(3)
#         self.driver.find_element_by_id("subject").send_keys("欢迎来到德莱联盟！！！")
#         sleep(3)
#         self.driver.find_element_by_name('message').send_keys("诺克萨斯即将崛起！！")
#         sleep(5)
#         self.driver.find_element_by_id("fastpostsubmit").click()
#         sleep(5)
#     def test_003shantie(self):
#         self.test_002post_a_message()
#         sleep(1)
#         self.driver.find_element_by_link_text("欢迎来到德莱联盟！！！").click()
#         self.driver.implicitly_wait(3)
#         self.driver.find_element_by_link_text("删除主题").click()
#         self.driver.implicitly_wait(3)
#         self.driver.find_element_by_name("modsubmit").click()
#     def test_004Management(self):
#         self.test_003shantie()
#         sleep(1)
#         mouse=self.driver.find_element_by_id("myprompt")
#         sleep(1)
#         ActionChains(self.driver).move_to_element(mouse).perform()
#         self.driver.find_element_by_xpath('//*[@id="myprompt_menu"]/li[3]/a').click()
#         sleep(1)
#         self.driver.find_element_by_link_text("现在处理").click()
#         sleep(2)
#         self.driver.find_element_by_name("admin_password").send_keys("123456")
#         sleep(1)
#         self.driver.find_element_by_name("submit").click()
#         sleep(2)
#         self.driver.implicitly_wait(3)
#         sleep(2)
#         self.driver.switch_to.frame(0)
#         self.driver.find_element_by_xpath('//*[@class="td25"]/input[1]').click()
#         sleep(1)
#         js = "window.scrollTo(0,500)"
#         self.driver.execute_script(js)
#         self.driver.find_element_by_name("delsubmit").click()
#     def tearDown(self) -> None:
#         self.driver.quit()
# if __name__ == '__main__':
#     unittest.main()
# 2.unittest框架第二种运行方式
# class Cms(unittest.TestCase):
#     def setUp(self) -> None:
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://192.168.93.128/bbs")
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(2)
#     def test_001register(self):
#         self.driver.find_element_by_id('ls_username').send_keys('admin')
#         self.driver.find_element_by_id('ls_password').send_keys('123456')
#         sleep(1)
#         self.driver.find_element_by_xpath("//*[@type='submit']/em[1]").click()
#         sleep(1)
#     def test_002post_a_message(self):
#         self.test_001register()
#         self.driver.find_element_by_link_text("默认版块").click()
#         sleep(2)
#         js="window.scrollTo(0,500)"
#         self.driver.execute_script(js)
#         sleep(3)
#         self.driver.find_element_by_id("subject").send_keys("欢迎来到德莱联盟！！！")
#         sleep(3)
#         self.driver.find_element_by_name('message').send_keys("诺克萨斯即将崛起！！")
#         sleep(5)
#         self.driver.find_element_by_id("fastpostsubmit").click()
#         sleep(5)
#     def test_003shantie(self):
#         self.test_002post_a_message()
#         sleep(1)
#         self.driver.find_element_by_link_text("欢迎来到德莱联盟！！！").click()
#         self.driver.implicitly_wait(3)
#         self.driver.find_element_by_link_text("删除主题").click()
#         self.driver.implicitly_wait(3)
#         self.driver.find_element_by_name("modsubmit").click()
#     def test_004Management(self):
#         self.test_003shantie()
#         sleep(1)
#         mouse=self.driver.find_element_by_id("myprompt")
#         sleep(1)
#         ActionChains(self.driver).move_to_element(mouse).perform()
#         self.driver.find_element_by_xpath('//*[@id="myprompt_menu"]/li[3]/a').click()
#         sleep(1)
#         self.driver.find_element_by_link_text("现在处理").click()
#         sleep(2)
#         self.driver.find_element_by_name("admin_password").send_keys("123456")
#         sleep(1)
#         self.driver.find_element_by_name("submit").click()
#         sleep(2)
#         self.driver.implicitly_wait(3)
#         sleep(2)
#         self.driver.switch_to.frame(0)
#         self.driver.find_element_by_xpath('//*[@class="td25"]/input[1]').click()
#         sleep(1)
#         js = "window.scrollTo(0,500)"
#         self.driver.execute_script(js)
#         self.driver.find_element_by_name("delsubmit").click()
#     def tearDown(self) -> None:
#         self.driver.quit()
# def case():
#    suite=unittest.TestSuite()
#    suite.addTests([Cms("test_001register"),Cms("test_002post_a_message"),Cms("test_003shantie"),Cms("test_004Management")])
#    return suite
# runner=unittest.TextTestRunner()
# runner.run(case())

# # 3、unittest框架第三种运行方式
# from UI_auto.HTMLTestRunner3_New import HTMLTestRunner
# class Cms(unittest.TestCase):
#     def setUp(self) -> None:
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://192.168.93.128/bbs")
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(2)
#     def test_001register(self):
#         self.driver.find_element_by_id('ls_username').send_keys('admin')
#         self.driver.find_element_by_id('ls_password').send_keys('123456')
#         sleep(1)
#         self.driver.find_element_by_xpath("//*[@type='submit']/em[1]").click()
#         sleep(1)
#     def test_002post_a_message(self):
#         self.test_001register()
#         self.driver.find_element_by_link_text("默认版块").click()
#         sleep(2)
#         js="window.scrollTo(0,1000)"
#         self.driver.execute_script(js)
#         sleep(1)
#         self.driver.find_element_by_id("subject").send_keys("欢迎来到德莱联盟！！！")
#         sleep(1)
#         self.driver.find_element_by_name('message').send_keys("诺克萨斯即将崛起！！")
#         sleep(1)
#         self.driver.find_element_by_id("fastpostsubmit").click()
#         sleep(1)
#     def test_003reply(self):
#         self.test_002post_a_message()
#         self.driver.find_element_by_class_name('fastre').click()
#         self.driver.find_element_by_xpath("//*[@id='postmessage']").send_keys("哈哈")
#         js = "window.scrollTo(0,1000)"
#         self.driver.execute_script(js)
#         self.driver.find_element_by_xpath("//*[@id='postsubmit']/span").click()
#         self.driver.find_element_by_xpath('//*[@id="mn_forum"]/a').click()
#     def test_004shantie(self):
#         self.driver.find_element_by_link_text("默认版块").click()
#         self.test_002post_a_message()
#         sleep(1)
#         self.driver.find_element_by_link_text("欢迎来到德莱联盟！！！").click()
#         self.driver.implicitly_wait(1)
#         self.driver.find_element_by_link_text("删除主题").click()
#         self.driver.implicitly_wait(1)
#         self.driver.find_element_by_name("modsubmit").click()
#     def test_005Management(self):
#         self.test_004shantie()
#         sleep(1)
#         mouse=self.driver.find_element_by_id("myprompt")
#         sleep(1)
#         ActionChains(self.driver).move_to_element(mouse).perform()
#         self.driver.find_element_by_xpath('//*[@id="myprompt_menu"]/li[3]/a').click()
#         sleep(1)
#         self.driver.find_element_by_link_text("现在处理").click()
#         sleep(2)
#         # self.driver.find_element_by_name("admin_password").send_keys("123456")
#         # sleep(1)
#         # self.driver.find_element_by_name("submit").click()
#         sleep(1)
#         self.driver.implicitly_wait(3)
#         sleep(1)
#         self.driver.switch_to.frame(0)
#         self.driver.find_element_by_xpath('//*[@class="td25"]/input[1]').click()
#         sleep(1)
#         js = "window.scrollTo(0,500)"
#         self.driver.execute_script(js)
#         self.driver.find_element_by_name("delsubmit").click()
#     # def
#     def tearDown(self) -> None:
#         self.driver.quit()
#
# if __name__ == '__main__':
#     file=r"D:\duoceshi\UI_auto\UI自动化测试报告.html"
#     f=open(file,"wb")
#     start_dir=r'D:\duoceshi\UI_auto'
#     discove=unittest.defaultTestLoader.discover(start_dir=start_dir,pattern="lesson*.py")
#     runner=HTMLTestRunner(stream=f,
#                           title="BBS_UI自动化测试报告",
#                           description="用例执行情况如下：",
#                           tester="李"
#                           )
#     runner.run(discove)
#
#





# # CMS环境用例
# import unittest
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# driver=webdriver.Chrome()
# driver.get("http://192.168.93.128:8080/cms/manage/login.do")
# driver.maximize_window()
# # 1.登录
# driver.find_element_by_id("userAccount").send_keys("admin")
# driver.find_element_by_id("loginPwd").send_keys("123456")
# driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
# sleep(2)
# # 2.进入用户管理中心
# driver.find_element_by_xpath('//*[@id="menu-user"]/dt/i').click()
# sleep(1)
# driver.find_element_by_xpath('//*[@id="menu-user"]/dd/ul/li[1]/a').click()
# # 3.添用户
# iframe=driver.find_element_by_xpath('//*[@id="iframe_box"]/div[2]/iframe')
# driver.switch_to.frame(iframe)
# driver.find_element_by_xpath('/html/body/div/div[2]/span[1]/a[2]').click()
# iframe1=driver.find_element_by_xpath('//*[@id="xubox_iframe1"]')
# driver.switch_to.frame(iframe1)
# driver.find_element_by_xpath('//*[@id="userName"]').send_keys('LLF')
# # driver.find_element_by_xpath('//*[@id="sysUserForm"]/table/tbody/tr[2]/td/label[1]').click()
# driver.find_element_by_xpath('//*[@id="user-tel"]').send_keys('18375684719')
# driver.find_element_by_xpath('//*[@id="user-email"]').send_keys('867985436@qq.com')
# driver.find_element_by_xpath('//*[@id="userAccount"]').send_keys('root')
# driver.find_element_by_xpath('//*[@id="loginPwd"]').send_keys('123456')
# driver.find_element_by_xpath('//*[@id="confirmPwd"]').send_keys('123456')
# driver.find_element_by_xpath('//*[@id="submitBtn"]').click()
# driver.switch_to.default_content()
#
# # 4.删除用户
# sleep(3)
# iframe=driver.find_element_by_xpath('//*[@id="iframe_box"]/div[2]/iframe')
# driver.switch_to.frame(iframe)
# # driver.find_element_by_xpath('//*[@id="searchValue"]').send_keys('LLF')
# # driver.find_element_by_xpath('//*[@id="searchBtn"]').click()
# driver.find_element_by_xpath('//*[@id="sysUserTab"]/tr[1]/td[1]/input').click()
# driver.find_element_by_xpath('//*[@id="sysUserTab"]/tr[1]/td[9]/a[4]/i').click()
# driver.find_element_by_xpath('//*[@id="xubox_layer1"]/div[1]/span[2]/a[1]').click()
# driver.switch_to.default_content()
# # 5.栏目管理
# sleep(1)
# driver.find_element_by_xpath('//*[@id="menu-system"]').click()
# driver.find_element_by_xpath('//*[@id="menu-system"]/dd/ul/li[1]/a').click()
# iframe2=driver.find_element_by_xpath('//*[@id="iframe_box"]/div[3]/iframe')
# driver.switch_to.frame(iframe2)
# sleep(1)
# driver.find_element_by_xpath('/html/body/div/div[1]/span[1]/a').click()
# # driver.switch_to.default_content()
# iframe3=driver.find_element_by_xpath('//*[@id="xubox_iframe1"]')
# driver.switch_to.frame(iframe3)
# sleep(1)
# driver.find_element_by_xpath('//*[@id="categoryName"]').send_keys('duoceshi')
# driver.find_element_by_xpath('//*[@id="categoryCode"]').send_keys('四川成都')
# driver.find_element_by_xpath('//*[@id="saveCategoryForm"]/table/tbody/tr[3]/td[2]/textarea').send_keys('成都多测师11班')
# driver.find_element_by_xpath('//*[@id="saveCategoryForm"]/table/tbody/tr[4]/td[2]/textarea').send_keys('haha')
# driver.find_element_by_xpath('//*[@id="saveCategoryForm"]/table/tbody/tr[5]/td[2]/textarea').send_keys('欢迎来到多测师')
# driver.find_element_by_xpath('//*[@id="saveCategoryForm"]/table/tbody/tr[6]/td[2]/textarea').send_keys('多测师')
# driver.find_element_by_xpath('//*[@id="submitBtn"]').click()
# driver.switch_to.default_content()
# # 6.删除栏目
# sleep(1)
# iframe2=driver.find_element_by_xpath('//*[@id="iframe_box"]/div[3]/iframe')
# driver.switch_to.frame(iframe2)
# sleep(1)
# driver.find_element_by_xpath('//*[@id="categoryTable"]/tr/td[1]/input').click()
# driver.find_element_by_xpath('//*[@id="categoryTable"]/tr/td[10]/a[2]/i').click()
# driver.find_element_by_xpath('//*[@id="xubox_layer1"]/div[1]/span[2]/a[1]').click()
# driver.switch_to.default_content()
# # 7.退出登录
# sleep(2)
# driver.find_element_by_xpath('/html/body/header/span[2]/a').click()
#
from UI_auto.HTMLTestRunner3_New import HTMLTestRunner
class Cms(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome()
        self.driver.get("http://192.168.93.128:8080/cms/manage/login.do")
        self.driver.maximize_window()
        sleep(1)
    def test_001denglu(self):       #登录
        self.driver.find_element_by_id("userAccount").send_keys("admin")
        self.driver.find_element_by_id("loginPwd").send_keys("123456")
        self.driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
        sleep(1)
    def test_002user(self):     #进入用户管理界面
        self.test_001denglu()
        self.driver.find_element_by_xpath('//*[@id="menu-user"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menu-user"]/dd/ul/li[1]/a').click()
    def test_003aaduser(self):      #添加用户
        self.test_002user()
        iframe=self.driver.find_element_by_xpath('//*[@id="iframe_box"]/div[2]/iframe')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/span[1]/a[2]').click()
        iframe1=self.driver.find_element_by_xpath('//*[@id="xubox_iframe1"]')
        self.driver.switch_to.frame(iframe1)
        self.driver.find_element_by_xpath('//*[@id="userName"]').send_keys('LLF')
        # driver.find_element_by_xpath('//*[@id="sysUserForm"]/table/tbody/tr[2]/td/label[1]').click()
        self.driver.find_element_by_xpath('//*[@id="user-tel"]').send_keys('18375684719')
        self.driver.find_element_by_xpath('//*[@id="user-email"]').send_keys('867985436@qq.com')
        self.driver.find_element_by_xpath('//*[@id="userAccount"]').send_keys('root')
        self.driver.find_element_by_xpath('//*[@id="loginPwd"]').send_keys('123456')
        self.driver.find_element_by_xpath('//*[@id="confirmPwd"]').send_keys('123456')
        self.driver.find_element_by_xpath('//*[@id="submitBtn"]').click()
        self.driver.switch_to.default_content()
        sleep(2)
        iframe=self.driver.find_element_by_xpath('//*[@id="iframe_box"]/div[2]/iframe')
        self.driver.switch_to.frame(iframe)
        # driver.find_element_by_xpath('//*[@id="searchValue"]').send_keys('LLF')
        # driver.find_element_by_xpath('//*[@id="searchBtn"]').click()
        self.driver.find_element_by_xpath('//*[@id="sysUserTab"]/tr[1]/td[1]/input').click()
        self.driver.find_element_by_xpath('//*[@id="sysUserTab"]/tr[1]/td[9]/a[4]/i').click()
        self.driver.find_element_by_xpath('//*[@id="xubox_layer1"]/div[1]/span[2]/a[1]').click()
        self.driver.switch_to.default_content()
    def test_004column(self):   #栏目管理
        self.test_003aaduser()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="menu-system"]').click()
        self.driver.find_element_by_xpath('//*[@id="menu-system"]/dd/ul/li[1]/a').click()
        iframe2=self.driver.find_element_by_xpath('//*[@id="iframe_box"]/div[3]/iframe')
        self.driver.switch_to.frame(iframe2)
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div/div[1]/span[1]/a').click()
        # driver.switch_to.default_content()
        iframe3=self.driver.find_element_by_xpath('//*[@id="xubox_iframe1"]')
        self.driver.switch_to.frame(iframe3)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="categoryName"]').send_keys('duoceshi')
        self.driver.find_element_by_xpath('//*[@id="categoryCode"]').send_keys('四川成都')
        self.driver.find_element_by_xpath('//*[@id="saveCategoryForm"]/table/tbody/tr[3]/td[2]/textarea').send_keys(
            '成都多测师11班')
        self.driver.find_element_by_xpath('//*[@id="saveCategoryForm"]/table/tbody/tr[4]/td[2]/textarea').send_keys('haha')
        self.driver.find_element_by_xpath('//*[@id="saveCategoryForm"]/table/tbody/tr[5]/td[2]/textarea').send_keys(
            '欢迎来到多测师')
        self.driver.find_element_by_xpath('//*[@id="saveCategoryForm"]/table/tbody/tr[6]/td[2]/textarea').send_keys('多测师')
        self.driver.find_element_by_xpath('//*[@id="submitBtn"]').click()
        self.driver.switch_to.default_content()
        sleep(1)
        iframe2=self.driver.find_element_by_xpath('//*[@id="iframe_box"]/div[3]/iframe')
        self.driver.switch_to.frame(iframe2)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="categoryTable"]/tr/td[1]/input').click()
        self.driver.find_element_by_xpath('//*[@id="categoryTable"]/tr/td[10]/a[2]/i').click()
        self.driver.find_element_by_xpath('//*[@id="xubox_layer1"]/div[1]/span[2]/a[1]').click()
        self.driver.switch_to.default_content()
    def test_005quit(self):
        self.test_004column()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/header/span[2]/a').click()
if __name__ == '__main__':
    file=r"D:\duoceshi\UI_auto\UI自动化测试报告.html"
    f=open(file,"wb")
    start_dir=r'D:\duoceshi\UI_auto'
    discove=unittest.defaultTestLoader.discover(start_dir=start_dir,pattern="lesson2.py")
    runner=HTMLTestRunner(stream=f,
                          title="BBS_UI自动化测试报告",
                          description="用例执行情况如下：",
                          tester="李"
                          )
    runner.run(discove)