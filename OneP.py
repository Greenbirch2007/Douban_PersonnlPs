
# -*- coding:utf8 -*-

# 写个小脚本就搞定了！
import re
import urllib

import urllib.request
import time

import requests
from lxml import etree
from requests.exceptions import RequestException

from all_list import al


def get_first_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None





def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！
    big_list = []
    selector = etree.HTML(html)

    big_links = selector.xpath('//*[@id="page-content"]/div[1]/div/div/div[1]/div[1]/div[2]/div[1]/div/a/img/@src')
    small_links = selector.xpath('//*[@id="page-content"]/div[1]/div/div/div[1]/div[3]/div[2]/ul/li/a/img/@src')

    for item in small_links:
        i1 = re.sub(r"thumbnail","album",item)
        i2 = re.sub("/W85xH85","",i1)
        big_list.append(i2)

    for item in big_links:
        big_list.append(item)

    for download_pic in big_list:
        try:
            urllib.request.urlretrieve(download_pic, '/home/w/for_funny/%s' % (r'%s' % download_pic[-16:]))
            print(download_pic)
        except FileNotFoundError:
            print('图片下载有问题')







if __name__ == '__main__':
    for item in al:

        url = 'https://kutikomiya.jp/movie/av-idol/'+str(item)+'/'

        html = get_first_page(url)
        parse_html(html)


# //*[@id="page-content"]/div[1]/div/div/div[4]/div/div[2]/ul/li/div/div[2]/p[1]/a/@href
