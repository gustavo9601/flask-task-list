from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from .config import Config
from .auth import auth
from flask import Flask


def create_app():
    app = Flask(
        Config.APP_NAME,
        template_folder=Config.TEMPLATE_FOLDER,
        static_folder=Config.STATIC_FOLDER
    )
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{Config.USER}:{Config.PASSWORD}@{Config.HOST}/{Config.DATABASE}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Registrando los bluprints
    app.register_blueprint(auth)

    # Init bootstrap plugin flask
    bootstrap = Bootstrap(app)

    # Init database
    db = SQLAlchemy()
    db.init_app(app)

    return app
