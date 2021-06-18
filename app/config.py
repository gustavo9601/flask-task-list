from common import config

settings = config()['settings']

class Config:
    SECRET_KEY = settings['secret_key']
    PRODUCTION = settings['production']
    DEBUG = settings['debug']
    APP_NAME = settings['app_name']
    TEMPLATE_FOLDER = settings['template_folder']
    STATIC_FOLDER = settings['static_folder']
