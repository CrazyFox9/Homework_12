import json


def load_json_data(path):
    """ Загружает список постов из JSON файла """

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def search_posts(posts, text):
    """ Выводит найденные посты по вхождению """

    posts_founded = []

    for post in posts:
        if text.lower() in post["content"].lower():
            posts_founded.append(post)
    return posts_founded
