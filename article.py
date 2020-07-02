# coding=utf-8
# Created by JTProgru
# Date: 2019-10-27
# https://jtprog.ru/

__author__ = 'jtprogru'
__version__ = '0.0.1'
__author_email__ = 'mail@jtprog.ru'

from tagextractor import TagExtractor, get_bookmarks, get_comments, get_views, get_votes


class Article:
    def __init__(self, author_nick=None, author_url=None, post_title=None, publish_date=None, post_url=None):
        # <span class="user-info__nickname user-info__nickname_small">germn</span>
        self.author_nick = author_nick
        # <a href="https://habr.com/ru/users/germn/" class="post__user-info user-info" title="Автор публикации">
        self.author_url = author_url
        # <a href="https://habr.com/ru/post/473042/" class="post__title_link">Плюсы и минусы Django</a>
        self.post_title = post_title
        # <a href="https://habr.com/ru/post/473042/" class="post__title_link">Плюсы и минусы Django</a>
        self.post_url = post_url
        # <span class="post__time">25 октября 2019 в 11:42</span>
        self.publish_date = publish_date


# link = "https://habr.com/ru/post/468491/"
# f = requests.get(link)

# data_str = TagExtractor(f.text)
