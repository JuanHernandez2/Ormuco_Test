import collections
import sys


class LRUCache:
    """
    This is a dum implementation of an LRU Cache
    """

    def __init__(self, cache_capacity):
        self.cache = collections.OrderedDict()
        self.cache_capacity = cache_capacity


    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.cache_capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value

    
    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1