#!/usr/bin/env python
# coding=utf-8
# Created by JTProgru
# Date: 2019-10-27
# https://jtprog.ru/

__author__ = 'jtprogru'
__version__ = '0.0.1'
__author_email__ = 'mail@jtprog.ru'

import requests
from bs4 import BeautifulSoup
import hashlib as h
from time import sleep
from db import post_to_db
from utils import get_post_obj


def post_dumper(link):
    try:
        res = requests.get(link)
        s = BeautifulSoup(res.text, "lxml")
        prep_post = get_post_obj(s.article)
        pid = h.sha256(str(prep_post['post_body']).encode()).hexdigest()
        post_to_db(hash_id=pid, post=prep_post)

    except Exception:
        pass


def links_loader():
    with open("data/links.txt", "r+") as f:
        # print("LINK LOADS")
        return f.readlines()[:-1]


if __name__ == '__main__':
    links = links_loader()
    print("LINK COUNT: ", len(links))
    for li in links:
        sleep(1.6)
        post_dumper(li)
