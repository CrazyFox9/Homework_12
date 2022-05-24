from flask import Flask, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)  # регистрируем блупринт главной страницы
app.register_blueprint(loader_blueprint)  # регистрируем блупринт страницы загрузки поста


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run()
