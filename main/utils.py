import json
from exceptions import *
import logging

logging.basicConfig(filename='logger.log', level=logging.INFO)


def load_json_data(path):
    """ Загружает список постов из JSON файла """
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        logging.info("Проблема с открытием файла с постами")
        raise DataJsonError


def search_posts(posts, text):
    """ Выводит найденные посты по вхождению """

    posts_founded = []

    for post in posts:
        if text.lower() in post["content"].lower():
            posts_founded.append(post)
    return posts_founded
