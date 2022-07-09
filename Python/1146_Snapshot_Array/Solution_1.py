class SnapshotArray:
    # list of lists + binary_search
    def __init__(self, length: int):
        self.current_num = 0
        # [snapshot number, value]
        self.array = [[[0,0]] for _ in range(length)]
        
    def set(self, index: int, val: int) -> None:
        lastest_num = self.array[index][-1][0]
        if lastest_num == self.current_num:
            self.array[index][-1][1] = val
        else:
            self.array[index].append([self.current_num, val])
        
    def snap(self) -> int:
        self.current_num += 1
        return self.current_num - 1
    
    def get(self, index: int, snap_id: int) -> int:
        target_index_array = self.array[index]
        i = self.binary_search(target_index_array, snap_id)
        return self.array[index][i][1]
    
    def binary_search(self, array, snap_id):
        # [[0,1], [1,2], [2,3] ... ]
        low, high = 0, len(array)-1
        while low < high:
            mid = (low + 1 + high) // 2
            if array[mid][0] <= snap_id: low = mid
            else: high = mid - 1
        return low