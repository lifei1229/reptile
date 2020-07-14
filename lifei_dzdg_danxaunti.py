#coding = utf-8
import time
from selenium import webdriver
import os
import requests
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib import request
import lxml
import lxml.html
import numpy
import time
import re
# 定义下载函数
def download(url, filename):
    if os.path.exists(filename):
        print('file exists!')
        return
    try:
        r = requests.get(url, stream=True, timeout=60)
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
        print("download ok ")
        return filename
    except KeyboardInterrupt:
        if os.path.exists(filename):
            os.remove(filename)
        raise KeyboardInterrupt
    except Exception:
        print("download no ok ")
        traceback.print_exc()
        if os.path.exists(filename):
            os.remove(filename)

def url_open(url):
    res = request.Request(url)
    res.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134")
    html = request.urlopen(res, timeout=60).read()
    return html

# 隐式打开一个浏览器
def open_Explor():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=options)
    return driver







driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(8)  # 设置隐式等待时间
url="http://220.160.52.44:8080/mobile"
print(driver.get(url))  # 地址栏里输入网址



driver.find_element_by_xpath('//*[@id="oauth_uname_w"]').send_keys("18020769731")
driver.find_element_by_xpath('//*[@id="oauth_upwd_w"]').send_keys("comejiyoon1229")
# driver.find_element_by_xpath('//*[@id="imgid"]/div/ul/li[10]/div/div[1]/a')[].click()  #
# /html/body/main[2]/section[1]/div/div[4]/button[1]
driver.find_element_by_xpath("/html/body/main[2]/section[1]/div/div[4]/button[1]").click()
time.sleep(3)
# 自学
driver.find_element_by_xpath('//*[@id="select_one"]').click() 
time.sleep(3)
# 党章党规。。。。
driver.find_element_by_xpath('//*[@id="main"]/div/div[8]/div').click()
time.sleep(3)

# 单选题

driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]').click()
    # 进入答题界面
#     点击背题模式
driver.find_element_by_xpath('//*[@id="back-question"]').click()
# //*[@id="back-question"]
print(driver.find_element_by_xpath('//*[@id="main"]/div[2]').text)
print(driver.find_element_by_xpath('//*[@id="answer"]').text)

length=967
try:
    f = open(u"党章党规单选题.txt", "a+", encoding='utf-8')
    s = ""
    for i in range(length):
        time.sleep(3)


        print(i)
        #     点击背题模式
        driver.find_element_by_xpath('//*[@id="back-question"]').click()
        # //*[@id="back-question"]
        timu=driver.find_element_by_xpath('//*[@id="main"]/div[2]').text
        daan=driver.find_element_by_xpath('//*[@id="answer"]').text
        print(driver.find_element_by_xpath('//*[@id="main"]/div[2]').text)
        print(driver.find_element_by_xpath('//*[@id="answer"]').text)
        s+=timu+'\n\n'
        driver.find_element_by_xpath('//*[@id="next"]').click()
        if i%10==0 or i==length-1:

            f = open(u"党章党规单选题.txt", "a+", encoding='utf-8')
            f.write(s)
            print(s)
            s=''
            f.close()
except Exception:
    print("some wrong")













    # 进入答题界面



    # print("click  is ok ")
    # time.sleep(2)  # 等待2秒
    #
    #
    # try:
    #     hre = driver.find_element_by_xpath('//*[@id="imgid"]/div/ul/li[10]/div/a')
    # except:
    #     hre = driver.find_element_by_xpath('//*[@id="imgid"]/div/ul/li[10]/div/div[1]/a')
    # next_url=hre.get_attribute("href")
    # driver.get(next_url)
    #
    # # 设置下载的图片数量及进行下载
    # start = 1
    # end = 30
    # i=0
    # # for i in range(start,end + 1):
    # #     # 获取图片位置
    # # img = driver.find_elements_by_xpath(xpath)
    # print("333")
    # for num in range(start,end+1):
    #     html=driver.page_source
    #     a=re.findall(r'src="([^<]+?\.jpg)',html)
    #     print(a)
    #     try:
    #         if 'jpg' in a[0]:
    #             url=a[0].replace("amp;",'')
    #             print("url",url)
    #             img_name = url.split('/')[-1]
    #             filename = os.path.join(path_dir, img_name[-25:])
    #             download(url,filename)
    #             # print(num + 1, "存入成功")
    #         else:
    #             print(num + 1, "存入失败")
    #         driver.find_element_by_xpath('//*[@id="container"]/span[2]').click()  # 翻到下一页
    #         print("完成！")
    #         time.sleep(3)
    #         print(path+'%d/%d'%(num,end))
    #     except Exception:
    #         print("this is some bug")
    #         pass

# driver.quit()





# for ele in img:
#         #   获取图片链接
#     target_url = ele.get_attribute("src")
#     print(target_url)
#         #   设置图片名称。以图片链接中的名字为基础选取最后25个字节为图片名称。
#     img_name = target_url.split('/')[-1]
#     filename = os.path.join(path, img_name[-25:])
#     if "jpg" in filename:
#         download(target_url, filename)
# #     # 下一页
# #     next_page = driver.find_element_by_class_name("img-next").click()
#     time.sleep(3)
# #     # 显示进度
#     i=i+1
#     print('%d / %d' % (i, len(img)))

# 关闭浏览器








