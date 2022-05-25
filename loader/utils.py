import json
from config import UPLOAD_FOLDER, POST_PATH
from exceptions import *
import logging

logging.basicConfig(filename='logger.log', level=logging.INFO)


def save_picture(picture):
    """ Сохраняет картинку и возвращает путь к ней """

    allowed_types = ["jpg", "jpeg", "png", "gif"]
    picture_type = picture.filename.split(".")[-1]

    if picture_type not in allowed_types:
        logging.info(f"Неверный формат картинки! Допустимы только: {', '.join(allowed_types)}!")
        raise WrongImageType(f"Неверный формат картинки! Допустимы только: {', '.join(allowed_types)}!")

    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"

    picture.save(picture_path)

    return picture_path


def add_post(post_list, post):
    """ Добавляет новый пост в файл постов JSON """

    post_list.append(post)

    try:
        with open(POST_PATH, 'w', encoding='utf-8') as file:
            json.dump(post_list, file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError
