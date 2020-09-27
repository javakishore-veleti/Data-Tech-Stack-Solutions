import pkgutil
import importlib

from adapters.adapters_registry import AdapterRegistry
from common_api.app_constants import THIS_APP_PACKAGES_TO_LOAD

global adapter_registry
adapter_registry = None


def initialize_global_vars():
    global adapter_registry
    adapter_registry = AdapterRegistry()


def import_submodules(package, recursive=True):
    """ Import all submodules of a module, recursively, including subpackages

    :param recursive:
    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        if 'templates' in name or 'global_vars' in name or 'common_api' in name:
            continue
        full_name = package.__name__ + '.' + name
        if 'templates' in full_name or 'global_vars' in full_name or 'common_api' in full_name or 'common_api' in full_name:
            continue
        print(f"Package {full_name}")
        results[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            results.update(import_submodules(full_name))
    return results


def initialize_all_other_modules():
    for a_package in THIS_APP_PACKAGES_TO_LOAD:
        import_submodules(a_package)
    __all__ = []
    """
    for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
        __all__.append(module_name)
        _module = loader.find_module(module_name).load_module(module_name)
        globals()[module_name] = _module
    """


def get_adapter_registry():
    return adapter_registry
