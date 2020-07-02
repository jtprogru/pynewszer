#!/usr/bin/env python
# coding=utf-8
# Created by JTProgru
# Date: 2019-10-27
# https://jtprog.ru/

__author__ = 'jtprogru'
__version__ = '0.0.1'
__author_email__ = 'mail@jtprog.ru'

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


base_url = 'https://python-scripts.com/requests'


try:
    r = requests.head(base_url,
                      proxies={'https': 'https://178.16.152.254:3128'},
                      headers={'User-Agent': UserAgent().chrome})
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')


except requests.exceptions.ConnectionError:
    pass




