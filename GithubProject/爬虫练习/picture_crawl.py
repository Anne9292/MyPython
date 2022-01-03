#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: 千泷（杨婷）
# @Email: qianlong.yang@tuya.com
# @Time: 2021/12/29 21:51
# @File: picture_crawl

import os
import time
import random
import json
import requests
from fake_useragent import UserAgent


# 获取图片地址
def get_picture_urls(page_num, headers):
    pic_urls = []
    url = 'https://unsplash.com/napi/search/photos?query=nature&per_page=2&page={}&xp=feedback-loop-v2%3Aexperiment'.format(
        page_num)
    r = requests.get(url, headers=headers, timeout=5)
    time.sleep(random.uniform(2.1, 3.5))  # 随机生成下一个实数
    r.raise_for_status()  # 判断网络连接状态
    r.encoding = r.apparent_encoding  # 解决乱码问题
    all_info = json.loads(r.text)
    results = all_info['results']
    for result in results:
        href = result['urls']['full']
        pic_urls.append(href)
    return pic_urls


# 下载接口，下载图片
def save_picture(count, url, headers):
    r = requests.get(url, headers=headers, timeout=5)
    save_path = os.path.join(
        os.path.dirname(__file__),
        'picture/{}.jpg'.format(count))
    with open(save_path, 'wb') as f:
        f.write(r.content)


def main(count):
    ua = UserAgent(verify_ssl=False)
    headers = {'User-Agent': ua.random}
    for page in range(count):
        print('***************************共{}页，当前爬取第{}页***************************'.format(count, page+1))
        urls = get_picture_urls(page, headers)
        for url in urls:
            print("===>>>共{}张，当前爬取第{}张".format(len(urls), urls.index(url)))
            save_picture(urls.index(url)+1, url, headers)


if __name__ == '__main__':
    main(2)
