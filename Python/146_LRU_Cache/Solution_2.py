class LRUCache:
    """
    Runtime: 979 ms, faster than 78.89% of Python3 online submissions for LRU Cache.
    Memory Usage: 75.6 MB, less than 60.67% of Python3 online submissions for LRU Cache.
    """
    # OrderedDict
    def __init__(self, capacity: int):
        """
        The OrderedDict algorithm can handle frequent reordering operations better than dict. 
        As shown in the recipes below, 
        this makes it suitable for implementing various kinds of LRU caches.
        """
        self.cache_dict = OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key not in self.cache_dict:
            return -1
        self.cache_dict.move_to_end(key)
        return self.cache_dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict:
            del self.cache_dict[key]
        if self.capacity <= len(self.cache_dict):
            self.cache_dict.popitem(0)
        self.cache_dict[key] = value