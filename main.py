#!/usr/bin/env python
# coding=utf-8
# Created by JTProgru
# Date: 2019-10-27
# https://jtprog.ru/

__author__ = 'jtprogru'
__version__ = '0.0.1'
__author_email__ = 'mail@jtprog.ru'

from utils import *
import json

POST_RANGE = {
    'first': 1,
    'last': 473336,
}

main_url = 'https://habr.com/ru/post/'
post_list = []
for pid in range(473396, 413316, -1):
    post_list.append(get_post_by_id(pid=pid, base_url=main_url))

