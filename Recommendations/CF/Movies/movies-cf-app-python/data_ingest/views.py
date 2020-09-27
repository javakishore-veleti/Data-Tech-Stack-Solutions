from application.app_server import app
from application.app_url_constants import DATA_INGEST_LISTING


@app.route(DATA_INGEST_LISTING)
def data_ingest_list():
    return "Hello World"
