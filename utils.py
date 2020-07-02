# coding=utf-8
# Created by JTProgru
# Date: 2019-10-27
# https://jtprog.ru/

__author__ = 'jtprogru'
__version__ = '0.0.1'
__author_email__ = 'mail@jtprog.ru'

import requests
import json


def save_links(lin):
    with open('data/url_list.txt', "a") as f:
        f.write(lin)


def dump_post(post, name):
    f_name = 'posts/post_' + str(name) + '.json'
    with open(f_name, "w+") as f:
        json.dump(post, fp=f, ensure_ascii=False)
    print(f"Post saved in file: {f_name}")


def dump_all_posts(obj_):
    with open("data/dump_all_posts.dump", "a") as f:
        print(obj_, file=f)


def get_post_text(soup):
    """
    Получаем содержимое поста с его страницы
    Вытаскиваем из супа :div: с class: "post__text post__text-html js-mediator-article"
    В этом div содержится весь текст поста
    """
    art = soup.article
    post = art.div.find("div", attrs={"class": "post__text"})
    return post.text


def check_url(url):
    try:
        # r = requests.head(url, proxies={'https': 'https://178.16.152.254:3128'})
        r = requests.head(url)
        if r.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        pass


def get_post_obj(article):
    """
    Сбор данных из объекта soup.article
    Возвращает словарь заполненый необходимыми данными
    :param article: soup.article
    :return: post: dictionary
    """
    post = {}
    try:
        # Подготавливаем данные - вытаскиваем их из soup.article
        post_text = article.find("div", attrs={"id": "post-content-body"}).text
        author = article.find('a', attrs={"class": "post__user-info user-info"})
        pub_date = article.find("span", attrs={"class": "post__time"})
        hubs = article.find_all('a', attrs={'class': 'inline-list__item-link hub-link'})
        post_tags = article.find_all('a', attrs={'class': 'inline-list__item-link post__tag', 'rel': 'tag'})
        post['title'] = article.h1.text.strip('\n')
        post['author'] = author.text.strip()
        post['author_url'] = author.attrs['href']
        post['pub_date'] = pub_date.attrs['data-time_published']
        post['post_body'] = post_text
        post['post_hubs'] = [hub.text for hub in hubs]
        post['post_tags'] = [tg.text for tg in post_tags]

        return post

    except Exception:
        return post

        # soup = BeautifulSoup(r.text, 'html5lib')
        # post['pid'] = pid  # номер
        # if soup.find("span", attrs={"class": "post__title-text"}).text:
        #     post['title'] = soup.find("span", attrs={"class": "post__title-text"}).text
        # else:
        #     post['title'] = "ND"
        # if soup.find("span", attrs={"class": "user-info__nickname user-info__nickname_small"}).text:
        #     post['nickname'] = soup.find("span", attrs={"class": "user-info__nickname user-info__nickname_small"}).text
        # else:
        #     post['nickname'] = "ND"
        # if soup.find("a", attrs={"class": "post__user-info user-info"}, href=True)['href']:
        #     post['author_url'] = soup.find("a", attrs={"class": "post__user-info user-info"}, href=True)['href']
        # else:
        #     post['author_url'] = "ND"
        # if soup.find("span", attrs={"class": "post__time"}).text:
        #     post['publish_date'] = soup.find("span", attrs={"class": "post__time"}).text
        # else:
        #     post['publish_date'] = "ND"
        # if soup.find("span", attrs={"class": "post-stats__views-count"}).text:
        #     post['views'] = soup.find("span", attrs={"class": "post-stats__views-count"}).text
        # else:
        #     post['views'] = "ND"
        # if soup.find("meta", attrs={"name": "description"})['content']:
        #     post['description'] = soup.find("meta", attrs={"name": "description"})['content']
        # else:
        #     post['description'] = "ND"
        # if soup.find("div", attrs={"class": "post__body post__body_full"}).text:
        #     post['body'] = soup.find("div", attrs={"class": "post__body post__body_full"}).text
        # else:
        #     post['body'] = "ND"
        #
        # if post['pid'] is not "ND":
        #     print(f"[*] Post {post['pid']} loaded")


# этот велосипед я использую всегда для получения нужных мне кусков html-а
def generic_get(soup, search_tag, condition):
    l = []
    for e in soup.findAll(search_tag):
        d = dict(e.attrs)
        if condition(d):
            l.append(e)
    return l


# получаем текст поста
# def get_post_text(main_soup):
#     return generic_get(main_soup, "div", lambda d: d.get("class", [''])[0] == "post")[0].text


# получаем текст всех комментов
def get_comments_text(main_soup):
    return ' '.join([x.text for x in generic_get(main_soup,
                                                 "div",
                                                 lambda d: d.get("class", [''])[0] == "message")])

# def get_page_data(page_link):
#     values = []
#     articles = soup.findAll('article', attrs={'class': 'post post_preview'})
#     for a in articles:
#         t = a.find("span", {"class": "post__time"})
#         date = str_to_date(t.text)
#         views, votes, votes_up, votes_down, comments, link = 0, 0, 0, 0, 0, ""
#
#         link = a.find("a", {"class": "btn btn_x-large btn_outline_blue post__habracut-btn"})
#         # Remove #habracut from link
#         link_url = link['href'].split('#')[0]
#
#         footer = a.find("footer", {"class": "post__footer"})
#         spans = footer.findAll('span')
#         for sp in spans:
#             value = Str(str_to_ascii(sp.text)).to_int()
#             if sp['class'][0] == 'post-stats__views-count':
#                 views = value
#             if sp['class'][0] == 'voting-wjt__counter':
#                 votes = value
#                 html = Str(sp)
#                 # 'title="Общий рейтинг 12: ↑11 и ↓1">+10</span' => 19, 3
#                 votes_up = html.find_between('↑', ' ')
#                 votes_down = html.find_between('↓', '"')
#             if sp['class'][0] == 'post-stats__comments-count':
#                 comments = value
#
#         date_str = date.strftime("%Y-%m-%dT%H:%M:%S.000")
#         print("{},{},views:{},votes:{},up:{},down:{},comments:{}".format(date_str, link_url, views, votes, votes_up,
#                                                                          votes_down, comments))
#
#         values.append([date, views, votes, comments])
#
#     return values
