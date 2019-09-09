
# -*- coding:utf8 -*-

# 写个小脚本就搞定了！
import urllib

import requests
import time
from selenium import webdriver
from lxml import etree
import datetime


def get_first_page(url):


    driver.set_window_size(1200, 1200)  # 设置窗口大小
    driver.get(url)
    html = driver.page_source
    return html





def next_page():
    for i in range(1,20):  # selenium 循环翻页成功！
        driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a').click()
        time.sleep(1)
        html = driver.page_source
        return html



def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！
    selector = etree.HTML(html)

    pic_links = selector.xpath('//*[@id="content"]/div/div[1]/ul/li/div[1]/a/img/@src')
    for item in pic_links:
        try:
            book_cover = item

            urllib.request.urlretrieve(book_cover, '/home/w/for_funny/%s' % (r'%s' % book_cover[-16:]))
        except FileNotFoundError:
            print('图片下载有问题')





if __name__ == '__main__':
    driver = webdriver.Chrome()
    url = 'https://movie.douban.com/celebrity/1037221/photos/'

    html = get_first_page(url)
    parse_html(html)
    while True:
        html = next_page()
        parse_html(html)
        print(datetime.datetime.now())

