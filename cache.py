import pickle
from cache3 import SimpleDiskCache
from cache3.setting import (DEFAULT_TAG, DEFAULT_TIMEOUT)
from typing import (Any, Type, Union)
from pathlib import Path
from util.setting import CACHE_PATH

PATH: Type = Union[Path, str]

# Pour savegarder les valeurs en utilisant pickle
class Cache(SimpleDiskCache):
    """
    Cache for storing pd objects in cache
    """
    def __init__(self, directory: PATH = CACHE_PATH, *args, **kwargs) -> None:
        super().__init__(directory, *args, **kwargs)

    # faire le processing des valeurs avant la sauvgarde
    def set(self, key: str, value: Any, timeout: Any = DEFAULT_TIMEOUT, tag: Any = DEFAULT_TAG):
        SimpleDiskCache.set(self, key, pickle.dumps(value), timeout=timeout, tag=tag)

    # faire le processing de valeur après sa réoccupation
    def get(self, key: str, default: Any = None, tag: Any = DEFAULT_TAG) -> Any:
        result = SimpleDiskCache.get(self, key, default=default, tag=tag)
        if (result != None):
            result = pickle.loads(result)
        return result
