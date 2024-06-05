import os
import configparser as configParser

basedir = os.path.abspath(os.path.dirname(__file__))
config_file = os.path.join(basedir, 'config.ini')

config = configParser.ConfigParser()
config.read(config_file)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = 'static'
    STATIC_URL_PATH = 'app/static'

    WTF_CSRF_ENABLED = True

    try:
        SECRET_KEY = config['API_KEYS']['SECRET_KEY']
    except KeyError:
        raise KeyError('SECRET_KEY not found in config.ini')