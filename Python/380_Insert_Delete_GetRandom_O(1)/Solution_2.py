class RandomizedSet:
    """
    Runtime 484 ms / Beats 86.51%
    Memory 61.2 MB / Beats 74.27%
    """
    def __init__(self):
        def default_val():
            return -1
        self.val_dict = collections.defaultdict(default_val)
        self.val_list = []
        self.count = 0

    def insert(self, val: int) -> bool:
        if self.val_dict[val] != -1 : return False
        self.val_dict[val] = len(self.val_list)
        self.val_list.append(val)
        self.count += 1
        return True

    def remove(self, val: int) -> bool:
        if self.val_dict[val] == -1 : return False
        idx = self.val_dict[val]
        # change
        self.val_list[-1], self.val_list[idx] = self.val_list[idx], self.val_list[-1]
        self.val_dict[self.val_list[idx]] = idx
        # remove
        self.val_list.pop()
        self.val_dict.pop(val)
        self.count -= 1
        return True

    def getRandom(self) -> int:
        num = random.randint(0, self.count-1)
        return self.val_list[num]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()