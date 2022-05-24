import json
from config import UPLOAD_FOLDER, POST_PATH


def save_picture(picture):
    """ Сохраняет картинку и возвращает путь к ней """

    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(picture_path)

    return picture_path


def add_post(post_list, post):
    """ Добавляет новый пост в файл постов JSON """

    post_list.append(post)
    with open(POST_PATH, 'w', encoding='utf-8') as file:
        json.dump(post_list, file)
