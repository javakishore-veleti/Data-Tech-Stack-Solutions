from flask import Flask, send_from_directory
import os

from flask_sqlalchemy import SQLAlchemy

from application import settings, app_config
from flask import request, redirect, url_for, render_template, flash, session
import pathlib


def initialize_db(app):
    db = SQLAlchemy(app)
    settings.db = db
    return db


def initialize_app(app) -> Flask:
    # app.config.from_object('application.app_config')
    app.debug = app_config.DEBUG
    app.secret_key = app_config.SECRET_KEY
    app.config.setdefault('PORT_NO', app_config.APP_PORT_NO)
    app.config.setdefault('SERVER_NAME', app_config.SERVER_NAME)
    app.config.from_envvar('MOVIES_CF_APP_PYTHON_SETTINGS', silent=True)

    app.SQLALCHEMY_DATABASE_URI = app_config.SQLALCHEMY_DATABASE_URI
    app.SQLALCHEMY_TRACK_MODIFICATIONS = app_config.SQLALCHEMY_TRACK_MODIFICATIONS

    db = initialize_db(app)

    settings.app = app

    return app


root_path = pathlib.Path(__file__).parent.absolute()

app = Flask(__name__, root_path=root_path, )
app = initialize_app(app)


# from data_ingest.views import *


@app.route('/')
def home():
    return render_template('home/index.html')


@app.route('/login')
def login():
    if not session.get('logged_in'):
        session['logged_in'] = True
    return redirect('/')


@app.route('/logout')
def logout():
    if session.get('logged_in'):
        session['logged_in'] = None
    return redirect(url_for('home'))


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(port=app_config.APP_PORT_NO, debug=True, load_dotenv=True)
