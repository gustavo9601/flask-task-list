from common import config

settings = config()['settings']
connection = config()['db_connection']

class Config:
    SECRET_KEY = settings['secret_key']
    PRODUCTION = settings['production']
    DEBUG = settings['debug']
    APP_NAME = settings['app_name']
    TEMPLATE_FOLDER = settings['template_folder']
    STATIC_FOLDER = settings['static_folder']
    HOST = connection['host']
    USER = connection['user']
    PASSWORD = connection['password']
    DATABASE = connection['database']
