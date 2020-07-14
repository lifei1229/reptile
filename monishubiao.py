# coding:utf-8
import requests
from bs4 import BeautifulSoup      #bs4
import re
import pandas as pd
import urllib.request
from selenium import webdriver    #模拟鼠标点击
from selenium.webdriver.common.keys import Keys
import time

# 声明一个司机，司机是个Chrome类的对象
driver = webdriver.Chrome()
 
#driver = webdriver.Chrome(r"C:\Users\lifei\AppData\Local\Google\Chrome\Application\chromedriver")


# 让司机加载一个网页
driver.get("http://demo.ranzhi.org")
 
# 给司机3秒钟去打开
time.sleep(3)
 
# 开始登录
# 1. 让司机找用户名的输入框
we_account = driver.find_element_by_css_selector('#account')
we_account.clear()
we_account.send_keys("demo")
 
# 2. 让司机找密码的输入框
we_password = driver.find_element_by_css_selector('#password')
we_password.clear()
we_password.send_keys("demo")
 
# 3. 让司机找 登录按钮 并 单击
driver.find_element_by_css_selector('#submit').click()
time.sleep(3)