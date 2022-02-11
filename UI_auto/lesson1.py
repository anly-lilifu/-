#coding=utf-8
"""
Author:多测师_李立伏
time:2022-01-21 14:13
Wechat:xiaoshubass
website:www.duoceshi.cn
"""
# from selenium import webdriver
# from time import sleep
# sleep(1)
# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.maximize_window()
# # click:点击   send_keys():输入
# # 1、id定位
# # driver.find_element_by_id("kw").send_keys("python")
# # driver.find_element_by_id("su").click()
# # 2、name定位：
# # driver.find_element_by_name("wd").send_keys("爬虫")
# # 3、class定位：
# # driver.find_element_by_class_name("s_ipt").send_keys("哈哈哈")
# # 4、link_text定位：
# # driver.find_element_by_link_text("新闻").click()
# # 5、partial_link_text：模糊匹配定位
# # driver.find_element_by_partial_link_text("讲好冬奥故事 共赴冰雪之约").click()
# # 6、通过标签名称点位：
# # driver.find_element_by_tag_name("input").click()
# # s=driver.find_element_by_tag_name("input")
# # print(s)
# # for i in s:
# #     if i.get_attribute("id")=="kw":
# #        i.send_keys("python")
# # 7、xpath定位：格式：//*[@]
# driver.find_element_by_xpath('//*[@id="s-top-left"]/a[7]').click()
# # # 8、css定位： id用#表示    class用.表示
# # driver.find_element_by_css_selector("#kw").send_keys("python")
# # sleep(1)
# # #组合定位：必须要满两个条件都相同才会被定位
# # driver.find_element_by_css_selector("[id=kw][slass=s_ipt]").send_keys("python")
#
# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.maximize_window()
# sleep(1)
# driver.find_element_by_id('s-usersetting-top'). click()
# sleep(1)
# driver.find_element_by_link_text("搜索设置").click()
# sleep(1)
# driver.find_element_by_link_text("保存设置").click()
# # alter=driver.switch_to_alert()
# #切换到a1ter弹框
# alter=driver.switch_to.alert
# # alter. dismiss() # 在alter弹框中点击取消
# sleep(2)
# alter.accept()  #并在alter弹框中点击确定
# #操作鼠标悬停:
# # from selenium.webdriver.common.action_chains import ActionChains#导入Actionchains这个类
# # driver=webdriver. Chrome ()
# # driver. get("http://www.jd.com")
# # driver. maximize_window()
# # mouse=driver.find_element_by_link_text("政企采购")# 定位元素
# # sleep(2)
# # #使用这个类传入driver对象， 并且将鼠标移动到指定元素的位置。 perform代表点击
# # ActionChains(driver).move_to_element(mouse).perform()
# # driver. find_element_by_link_text("大中型企业采购").click() # 选择展示框下面的内容
#
# #文件选择框:
# driver=webdriver.Chrome()
# driver.get("file:///D:/%E5%88%98%E5%BB%BA/%E5%A4%9A%E6%B5%8B%E5%B8%88%E8%B5%84%E6%96%99/%E8%AF%BE%E4%BB%B6/%E7%AC%AC%E4%BA%8C%E4%B8%AA%E6%9C%88%E8%AF%BE%E4%BB%B6/%E7%AC%AC%E4%BA%8")
# sleep(1)
# #定位元素，传入文件路径。表示 上传文件
# driver. find_element_by_id("file").send_keys(r'D:\刘建\多测师资料\刘建\atm机取钱控制流. jpg' )


# from selenium import webdriver
# from time import sleep
# sleep(2)
# driver=webdriver.Chrome()
# driver.get("http://www.wangyiyun.com")

#
# from time import sleep
# driver=webdriver.Chrome()
# sleep(3)
# driver.get("httt://www.baidu.com")
# 2.# 隐式等待：作用于全局的等待
# driver.implicitly_wait(20)
# 3.显示等待，作用于某个元素
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as a
# from  selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com")
# # 使driver在5秒钟之内等待某个元素出现。每隔0.5秒就去检查一次这个元素是否出现
# WebDriverWait(driver,5,poll_frequency=0.5).until(a.presence_of_all_elements_located((By.ID,"kw")))
# driver.find_element_by_id("kw").send_keys("python")

# 断言：判断运行的结果和我的预期结果是否一致
# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.maximize_window()
# a=driver.find_element_by_xpath("//*[@id='s-top-left']/a[1]").text
# # print(a)
# if a==("新闻"):
#     print("访问成功")
# else:
#     print("访问失败")
# 获取页面的标题：也可以用来断言
# title=driver.title
# driver.title  #获取标题的动作
# # print(title)
# # 获取网页窗口的大小：
# driver.maximize_window()
# size=driver.get_window_size()
# print(size)
# 对于窗口进行刷新：
# sleep(2)
# driver.find_element_by_id("kw").send_keys("爬虫")
# sleep(2)
# driver.refresh()   #刷新窗口
# #新开一个窗口：
# sleep(2)
# win="window.open('http://www.jd.com')"
# driver.execute_script(win)
# sleep(2)
# #关闭当前窗口
# driver.close()
# #关闭所有窗口
# driver.quit()

# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.find_element_by_link_text("hao123").click()
# print(driver.title)
# handle=driver.current_window_handle
# print(handle)
# handle1=driver.window_handles#取出所有窗口的句柄
# print(handle1)
# #第一种切换窗口的方法：通过列表的索引位
# driver.switch_to.window(handle1[-1])            #将主窗口切换到handle1列表的左后一个句柄的网页
# print(title)
# driver.find_element_by_name("word").send_keys("爬虫")
# # 第二种
# for i in handle1:
#     if i !=handle:
#         driver.switch_to.window(i)
# print(driver.title)

#下拉框选择：
# from selenium.webdriver.support.select import Select
# driver=webdriver.Chrome()
# driver.get("https://www.ctrip.com/")
# sleep(1)
# driver.maximize_window()
# sleep(1)
# S=driver.find_element_by_id("J_roomCountList")
# # 1、通过索引值进行操作
# Select(S).select_by_index(3)
# driver.close()  #关闭当前窗口
# # 2、通过文本内容进行操作
# driver=webdriver.Chrome()
# driver.get("https://www.ctrip.com/")
# sleep(1)
# driver.maximize_window()
# sleep(1)
# S=driver.find_element_by_id("J_roomCountList")
# Select(S).select_by_visible_text("5间")
# driver.close()  #关闭当前窗口
# # 3.通过value值进行操作
# driver=webdriver.Chrome()
# driver.get("https://www.ctrip.com/")
# sleep(1)
# driver.maximize_window()
# sleep(1)
# S=driver.find_element_by_id("J_roomCountList")
# Select(S).select_by_value("6")
# driver.close()  #关闭当前窗口
#alter弹框：
# driver=webdriver.Chrome()
# #获取alter弹框的文本信息：
#1.警告型：
# driver.get("file:///E:/%E5%BC%B9%E7%AA%97/alert.html")
# sleep(1)
# alter=driver.switch_to.alert
# # print(alter.text)
# sleep(1)
# alter.dismiss()# 点击取消
# sleep(2)
# alter.accept()  #点击确定

# 2、确认型//*[@id="modsubmit"]/span：
# driver.get('file:///E:/%E5%BC%B9%E7%AA%97/enter.html')
# driver.find_element_by_class_name("alert").click()
# sleep(1)
# alter=driver.switch_to.alert
# alter.accept()
#

# 3.输入型：
# driver.get('file:///E:/%E5%BC%B9%E7%AA%97/prompt.html')
# driver.find_element_by_class_name("alert").click()
# alter=driver.switch_to.alert
# sleep(1)
# alter.send_keys("百度")
# sleep(1)

# iframe框：
# driver=webdriver.Chrome()
# driver.get("https://mail.163.com/")
# driver.maximize_window()
#第一种进入iframe框的放法：
# iframe=driver.find_element_by_xpath('//*[@id="loginDiv"]/iframe[1]')
# driver.switch_to.frame(iframe)
#第二种，当只有一个iframe的时候：
# iframe=driver.find_element_by_tag_name("iframe")
# driver.switch_to.frame(iframe)
#第三种：通过iframe框的索引位来切换
# driver.switch_to.frame(0)
# sleep(2)
# driver.find_element_by_name("email").send_keys("18375684719")
# sleep(1)
# driver.find_element_by_name("password").send_keys("11111")
# sleep(1)
# driver.find_element_by_id("dologin").click()
# driver.switch_to.default_content()

#滑动滚动条
# driver=webdriver.Chrome()
# driver.get('https://www.jd.com/')
# driver.maximize_window()
# # js="window.scrollTo(0,2000)"
# # js1="window.scrollTo(0,2000)"
# # driver.execute_script(js)
# for i in  range(0,2000,20):
#     js="window.scrollTo(0,%d)%i"
#     driver.execute_script(js)

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from time import sleep
# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.maximize_window()
# driver.find_element_by_id("kw").send_keys("Pythonn")
# sleep(1)
# driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
# sleep(1)
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"a")
# sleep(1)
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"x")
# sleep(1)
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"v")












list1=[1,2,3,4,1,1,1,"hello","hello","china"]
print(list1) #[1, 2, 3, 4, 1, 1, 1, 'hello', 'hello']
