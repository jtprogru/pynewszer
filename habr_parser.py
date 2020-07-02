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
sitemap_url = 'https://habr.com/sitemap.xml'


def check_url(url):
    try:
        r = requests.head(url)
        if r.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        pass


def explore_sitemap(sitemap):
    res = requests.get(sitemap)
    s = BeautifulSoup(res.text, "html5lib")
    st = s.find_all("loc")
    sitemaps = [s.text for s in st]
    print(f'Find sitemaps: {str(len(sitemaps))}')
    return sitemaps


def get_links(urls):
    url_list = []
    for url in urls:
        if check_url(url):
            url_list.append(url)
    print(f'Returned links: {str(len(url_list))}')
    return url_list


def main():
    u = explore_sitemap(sitemap_url)
    ul = [l for l in u]
    smaps = get_links(ul)
    links = []

    for s in smaps:
        sm = explore_sitemap(s)
        links.append([l for l in sm])

    with open('data/links.txt', "a") as f:
        for li in links:
            for l in li:
                print(l, file=f)

    print(f"Total links count: {str(len(links))}")


if __name__ == '__main__':
    main()
