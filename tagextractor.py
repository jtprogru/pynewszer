# coding=utf-8
# Created by JTProgru
# Date: 2019-10-27
# https://jtprog.ru/

__author__ = 'jtprogru'
__version__ = '0.0.1'
__author_email__ = 'mail@jtprog.ru'


class TagExtractor(str):
    def find_between(self, first, last):
        try:
            start = self.index(first) + len(first)
            end = self.index(last, start)
            return TagExtractor(self[start:end])
        except ValueError:
            return TagExtractor("")

    def to_int(self):
        s = self.lower().replace(",", ".")
        if s[-1:] == "k":
            # "1.23k" => 1.23*1000 => 1230
            return int(1000*float(s.replace("k", "")))
        return int(self)


def get_votes(data_str: TagExtractor):
    return data_str.find_between(
        'span class="voting-wjt__counter voting-wjt__counter_positive  js-score"', 'span').find_between('>', '<')


def get_bookmarks(data_str: TagExtractor):
    return data_str.find_between('span class="bookmark__counter js-favs_count"', 'span').find_between('>', '<')


def get_views(data_str: TagExtractor):
    return data_str.find_between('span class="post-stats__views-count"', 'span').find_between('>', '<')


def get_comments(data_str: TagExtractor):
    return data_str.find_between('span class="post-stats__comments-count"', 'span').find_between('>', '<')


# str_out = "{},votes:{},bookmarks:{},views:{},comments:{};".format(timestamp,
#                                                                   str(votes.to_int()),
#                                                                   str(bookmarks.to_int()),
#                                                                   str(views.to_int()),
#                                                                   str(comments.to_int()))
#
# print(str_out)
