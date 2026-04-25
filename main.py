from collections import OrderedDict
from typing import Any

class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: OrderedDict[int, Any] = OrderedDict()

    def get(self, key: int) -> Any:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: Any) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, "A")
    cache.put(2, "B")
    print(cache.get(1))
    cache.put(3, "C")
    print(cache.get(2))
