# coding=utf-8
# Created by JTProgru
# Date: 2019-10-31
# https://jtprog.ru/

__author__ = 'jtprogru'
__version__ = '0.0.1'
__author_email__ = 'mail@jtprog.ru'

import dotenv as d
from pathlib import Path
import psycopg2
env = d.get_variables(str(Path(__file__).parent / '.env'))


def post_to_db(hash_id, post):
    try:
        connection = psycopg2.connect(dbname=env['DB_NAME'], user=env['DB_USER'],
                                      password=env['DB_PASS'], host=env['DB_HOST'])
        cursor = connection.cursor()

        postgres_insert_query = """INSERT INTO habr_posts (title, author, author_url, post_body, post_hubs, post_tags, pub_date) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (post['title'], post['author'], post['author_url'], post['post_body'], post['post_hubs'], post['post_tags'], post['pub_date'])
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(f"{count} post inserted: {hash_id}")

    except (Exception, psycopg2.Error) as error:
        if connection:
            print("Failed to insert record into table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
