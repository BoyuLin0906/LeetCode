class Node:
    def __init__(self, key=0, value=0):
        #  --- |prev [key/value] next| --- |prev [key/value] next| ---
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """
    Runtime: 936 ms, faster than 84.50% of Python3 online submissions for LRU Cache.
    Memory Usage: 75.3 MB, less than 67.17% of Python3 online submissions for LRU Cache.
    """
    # doubly-linked-list
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_dict = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.cache_dict: return -1
        node = self.cache_dict[key]
        self._update(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict:
            self._remove(self.cache_dict[key])
        
        node = Node(key, value)
        self._add(node)
        self.cache_dict[key] = node
        
        if len(self.cache_dict) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.cache_dict[node.key]
        
    def _remove(self, node):
        # before: prev_node --- node --- next_node
        # after:  prev_node --- next_node
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
    def _add(self, node):
        # before: prev_node --- tail_node
        # after: prev_node --- node --- tail_node
        prev_node = self.tail.prev
        prev_node.next = node
        self.tail.prev = node
        node.prev = prev_node
        node.next = self.tail
    
    def _update(self, node):
        # before: ... --- node --- ...
        # after: node --- tail_node
        self._remove(node)
        self._add(node)
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)