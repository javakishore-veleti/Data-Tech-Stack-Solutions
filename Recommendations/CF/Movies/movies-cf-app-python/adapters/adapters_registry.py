from common_api.adapters import AppAdapter, SparkSubmissionAdapter


class AdapterRegistry:
    def __init__(self):
        self.adapters_registry = {}

    def get_adapter_by_key(self, registry_key: str) -> AppAdapter:
        if registry_key in self.adapters_registry:
            return self.adapters_registry[registry_key]
        return None

    def get_spark_adapter_by_key(self, registry_key: str) -> SparkSubmissionAdapter:
        if registry_key in self.adapters_registry:
            return self.adapters_registry[registry_key]
        return None

    def register_adapter_impl(self, registry_key: str, adapter_impl: AppAdapter):
        self.adapters_registry.update({registry_key: adapter_impl})

    def spark_register_adapter_impl(self, registry_key: str, adapter_impl: SparkSubmissionAdapter):
        self.register_adapter_impl(registry_key, adapter_impl)
