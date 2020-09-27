from flask import render_template

from common_api import global_vars
from common_api.global_vars import adapter_registry
from common_api.adapter_contants import SPARK_JOB_ADAPTER_DEFAULT
from common_api.dto import SparkJobExecInfo


def create_movies_cf_ml_model():
    # return "Hello World download_movies_data"

    wf_exec_info: SparkJobExecInfo = SparkJobExecInfo()
    adapter_registry.get_spark_adapter_by_key(SPARK_JOB_ADAPTER_DEFAULT).execute_spark_job(wf_exec_info)
    return render_template('ml_model_dev/create_movies_cf_message.html')
