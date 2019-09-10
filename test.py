
import urllib.request

import requests

url = 'https://fanhao.mmdaren.com/UpLoad/2014/03-10/24d2134b423841f18b98f0288e5b9afa.jpg'

from selenium import webdriver


image_path = '/home/w/for_funny/%s.jpg'
image_data=urllib.request.urlopen(url).read()    #获取图片信息
with open(image_path,"wb") as image_file:
    image_file.write(image_data)