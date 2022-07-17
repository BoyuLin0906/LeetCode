class LRUCache:
    """
    Runtime: 2689 ms, faster than 7.55% of Python3 online submissions for LRU Cache.
    Memory Usage: 74.5 MB, less than 95.65% of Python3 online submissions for LRU Cache.
    """
    # dict + array
    def __init__(self, capacity: int):
        self.stack_dict = {}
        self.stack = []
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.stack_dict:
            self.stack.remove(key)
            self.stack.append(key)
            return self.stack_dict[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.stack_dict:
            self.stack.remove(key)
        else:
            if self.capacity <= len(self.stack):
                tmp_key = self.stack.pop(0)
                del self.stack_dict[tmp_key]
        self.stack_dict[key] = value
        self.stack.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)