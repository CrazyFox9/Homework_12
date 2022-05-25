from flask import Blueprint, render_template, request
from main.utils import *
from config import POST_PATH

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

logging.basicConfig(filename='logger.log', level=logging.INFO)


@main_blueprint.route('/')
def main_page():
    """ Главная страница сайта """

    logging.info("Открытие главной страницы")
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    """ Страница найденных постов по вхождению слова """

    s = request.args.get("s", "")

    logging.info(f"Выполнен поиск: {s}")

    try:
        posts = load_json_data(POST_PATH)
    except DataJsonError:
        return "Проблема с открытием файла с постами"

    filtered_posts = search_posts(posts, s)

    return render_template('post_list.html', posts=filtered_posts, s=s)
