from flask import render_template


def data_ingest_list():
    return "Hello World"


def download_movies_data():
    return render_template('data_ingest/download_movies_data_msg.html')
