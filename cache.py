import sys

assert sys.version_info >= (3, 7), "Use Python 3.7 or newer"


class LRUCache:
    def __init__(self, capacity: int = 10) -> None:
        if not isinstance(capacity, int):
            raise TypeError("capacity must be int")
        elif capacity <= 0:
            raise ValueError("capacity must be positive")
        self._capacity = capacity
        self._dict = dict()

    def get(self, key: str) -> str:
        if not isinstance(key, str):
            raise TypeError("key and must be string")
        if key not in self._dict:
            return ''
        value = self._dict.pop(key)
        self._dict[key] = value
        return value

    def set(self, key: str, value: str) -> None:
        if not isinstance(key, str) or not isinstance(value, str):
            raise TypeError("key and value must be strings")
        if key in self._dict:
            del self._dict[key]
        elif len(self._dict) == self._capacity:
            del self._dict[next(iter(self._dict))]
        self._dict[key] = value

    def rem(self, key: str) -> None:
        self._dict.pop(key, None)
