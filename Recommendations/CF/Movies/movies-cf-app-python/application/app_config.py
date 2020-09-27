import os

APP_PORT_NO = int(os.getenv("ENV_APP_PORT_NO", 5000))
DEBUG = os.getenv("ENV_DEBUG", True)
SERVER_NAME = os.getenv("ENV_SERVER_NAME", '0.0.0.0')
SECRET_KEY = 'Some Secret Key'

SQLALCHEMY_DATABASE_URI = 'sqlite:///db_movies_cf_app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

