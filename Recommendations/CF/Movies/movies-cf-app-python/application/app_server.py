from flask import Flask, send_from_directory
import os

from flask_sqlalchemy import SQLAlchemy

from application import settings, app_config
from flask import request, redirect, url_for, render_template, flash, session
import pathlib

from application.app_url_constants import DATA_INGEST_LISTING, DATA_INGEST_MOVIES_DATA_DOWNLOAD, \
    ML_MODEL_DEV_CREATE_CF_ML_MODEL
from common_api.global_vars import initialize_global_vars, initialize_all_other_modules


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


initialize_global_vars()
initialize_all_other_modules()


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if not session.get('logged_in'):
        session['logged_in'] = True
    return redirect('/')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if session.get('logged_in'):
        session['logged_in'] = None
    return redirect(url_for('home'))


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


from data_ingest import views as data_ingest_views
from ml_model_dev import views as ml_model_dev_views

app.add_url_rule(DATA_INGEST_LISTING, view_func=data_ingest_views.data_ingest_list)
app.add_url_rule(DATA_INGEST_MOVIES_DATA_DOWNLOAD, view_func=data_ingest_views.download_movies_data)
app.add_url_rule(ML_MODEL_DEV_CREATE_CF_ML_MODEL, view_func=ml_model_dev_views.create_movies_cf_ml_model)


if __name__ == '__main__':
    app.run(port=app_config.APP_PORT_NO, debug=True, load_dotenv=True)
