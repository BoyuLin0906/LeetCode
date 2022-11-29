class RandomizedSet:
    """
    Runtime 1803 ms / Beats 6.90%
    Memory 61.1 MB / Beats 85.64%
    """
    def __init__(self):
        self.val_set = set()
        self.count = 0

    def insert(self, val: int) -> bool:
        if val in self.val_set: return False
        self.val_set.add(val)
        self.count += 1
        return True

    def remove(self, val: int) -> bool:
        if not val in self.val_set: return False
        self.val_set.remove(val)
        self.count -= 1
        return True

    def getRandom(self) -> int:
        num = random.randint(0, self.count-1)
        return list(self.val_set)[num]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()