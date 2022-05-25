from flask import Blueprint, render_template, request
from main.utils import *
from loader.utils import *
from config import POST_PATH

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

logging.basicConfig(filename='logger.log', level=logging.INFO)


@loader_blueprint.route('/post')
def create_new_post_page():
    """ Страницы загрузки нового поста """

    logging.info("Открыта страница загрузки нового поста")
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def created_new_post_by_user():
    """ Страница нового поста """

    picture = request.files.get("picture")
    content = request.form.get("content")

    if not picture or not content:
        logging.info("Отсутствует часть данных")
        return "Отсутствует часть данных"

    posts = load_json_data(POST_PATH)

    try:
        new_post = {"pic": save_picture(picture), "content": content}
    except WrongImageType:
        return "Неверный формат картинки!"

    add_post(posts, new_post)

    logging.info("Добавлен новый пост")

    return render_template('post_uploaded.html', new_post=new_post)
