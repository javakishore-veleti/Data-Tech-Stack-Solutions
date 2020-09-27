from common_api.adapter_contants import SPARK_JOB_ADAPTER_DEFAULT


class WFCtxData:
    ctx_data = {}

    def add_data(self, key: str, value):
        self.ctx_data.update({key, value})

    def get_ctx_data(self, key: str):
        if key in self.ctx_data:
            return self.ctx_data.update({key})
        return None

    def has_key(self, key: str):
        return key in self.ctx_data

    def remove_data(self, key: str):
        if key in self.ctx_data:
            self.ctx_data.pop(key)
        return


class WFExecInfo(WFCtxData):
    pass


class WFExecResult(WFCtxData):
    pass


class SparkJobExecInfo(WFExecInfo):
    job_name: str = None
    adapter_to_use: str = None

    def __init__(self):
        self.job_name = "Undefined"
        self.adapter_to_use = SPARK_JOB_ADAPTER_DEFAULT
