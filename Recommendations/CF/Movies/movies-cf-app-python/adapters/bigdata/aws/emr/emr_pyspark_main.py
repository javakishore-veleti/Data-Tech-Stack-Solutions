from common_api.adapter_contants import SPARK_JOB_ADAPTER_DEFAULT, SPARK_JOB_ADAPTER_AWS_EMR
from common_api.adapters import SparkSubmissionAdapter
from common_api.dto import SparkJobExecInfo
from common_api.global_vars import get_adapter_registry


class AwsEmrSparkSubmissionAdapterImpl(SparkSubmissionAdapter):

    def execute_spark_job(self, wf_exec_info: SparkJobExecInfo):
        pass


def register_adapter_impl():
    get_adapter_registry().register_adapter_impl(SPARK_JOB_ADAPTER_AWS_EMR, AwsEmrSparkSubmissionAdapterImpl())