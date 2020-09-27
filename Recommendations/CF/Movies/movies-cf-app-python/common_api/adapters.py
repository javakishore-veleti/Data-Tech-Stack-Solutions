from common_api.dto import SparkJobExecInfo, WFExecInfo


class AppAdapter:
    def execute(self, wf_exec_info: WFExecInfo):
        pass


class SparkSubmissionAdapter(AppAdapter):
    def execute_spark_job(self, wf_exec_info: SparkJobExecInfo):
        pass