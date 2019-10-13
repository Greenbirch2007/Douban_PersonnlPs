# _*_coding:utf-8_*_
from urllib.parse import urljoin
import requests
import re
import os
class GetImage(object):
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }
        self.dir_path = os.path.dirname(os.path.abspath(__file__))
        self.path = self.dir_path + '/imgs'
        isExists = os.path.exists(self.dir_path + '/imgs')
        # 创建目录
        if not isExists:
            os.makedirs(self.path)

    def download(self, url):
        try:
            res = requests.get(url, headers=self.headers)
            return res
        except Exception as E:
            print(url + '下载失败,原因:' + E)

    def parse(self, res):
        content = res.content.decode()
        # print(content)
        img_list = re.findall(r'<img.*?src="(.*?)"', content, re.S)
        img_list = [urljoin(self.url, url) for url in img_list]
        return img_list

    def save(self, res_img, file_name):
        if (file_name.endswith('jpg')) or (file_name.endswith('png')):
            file_name = file_name
        else:
            file_name = file_name + '.jpg'

        if res_img:
            with open(file_name, 'wb') as f:
                f.write(res_img.content)
            print(url + '下载成功')

    def run(self):
        # 下载
        res = self.download(self.url)
        # 解析
        url_list = self.parse(res)
        # 下载图片
        for url in url_list:
            res_img = self.download(url)
            name = url.strip().split('/').pop()
            file_name = self.path + '/' + name
            # 保存
            self.save(res_img, file_name)

if __name__ == '__main__':
    # url_list = ['https://fanhao.mmdaren.com/avnvyou/']
    url_list = ['https://www.meitulu.com/item/12002.html']

    for url in url_list:
        text = GetImage(url)
        text.run()
