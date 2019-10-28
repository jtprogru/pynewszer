#!/usr/bin/env python
# coding=utf-8
# Created by JTProgru
# Date: 2019-10-27
# https://jtprog.ru/

__author__ = 'jtprogru'
__version__ = '0.0.1'
__author_email__ = 'mail@jtprog.ru'

import requests
import hashlib
from time import sleep

base_url = 'https://habr.com/ru/post/'
url_list = []
itr = 0


def check_url(url):
    try:
        sleep(0.5)
        r = requests.head(url, proxies={'https': 'https://178.16.152.254:3128'})
        if r.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        pass


def save_url(urll):
    with open('data/url_list.txt', 'a') as f:
        f.writelines(f"{urll}\n")


for i in range(472454, 473454):
    url_ = base_url + str(i) + '/'
    if check_url(url_):
        itr += 1
        url_list.append(url_)
        h = hashlib.md5(url_.encode('utf-8')).hexdigest()
        fstr = f'[{itr}] URL: {url_} \n\tHASH: {h}'
        save_url(fstr)

print(len(url_list))


