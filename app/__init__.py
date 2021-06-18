from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config


def create_app():
    app = Flask(
        Config.APP_NAME,
        template_folder=Config.TEMPLATE_FOLDER,
        static_folder=Config.STATIC_FOLDER
    )
    app.config['SECRET_KEY'] = Config.SECRET_KEY

    # Init bootstrap plugin flask
    bootstrap = Bootstrap(app)

    return app
