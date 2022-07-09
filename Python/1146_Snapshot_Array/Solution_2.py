class SnapshotArray:

    def __init__(self, length: int):
        self.current_num = 0
        self.array = [collections.OrderedDict({0: 0}) for _ in range(length)]
        
    def set(self, index: int, val: int) -> None:
        self.array[index][self.current_num] = val
        
    def snap(self) -> int:
        self.current_num += 1
        return self.current_num - 1
    
    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.array[index]: return self.array[index][snap_id]
        keys = list(self.array[index].keys())
        i = self.binary_search(keys, snap_id)
        return self.array[index][keys[i]]
    
    def binary_search(self, array, snap_id):
        # [[0,1], [1,2], [2,3] ... ]
        low, high = 0, len(array)-1
        while low < high:
            mid = (low + 1 + high) // 2
            if array[mid] <= snap_id: low = mid
            else: high = mid - 1
        return low