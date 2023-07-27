#!/usr/bin/python3
"""FIFO cache"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache system """
    def __init__(self):
        """ Initialize class instance. """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add key/value pair to cache data. """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.queue.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Return value stored in `key` key of cache. """
        return self.cache_data.get(key)
