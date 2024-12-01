"""
Runtime 3 ms / Beats 57.43%
Memory 17.48 MB / Beats 5.25%
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        arr.sort()

        for idx in range(len(arr)):
            target = arr[idx] * 2
            target_idx = self.binary_search(arr, target)
            if target_idx >= 0 and target_idx != idx:
                return True

        return False

    def binary_search(self, arr, target):
        left_idx = 0
        right_idx = len(arr)-1

        while left_idx <= right_idx:

            mid_idx =  left_idx + (right_idx - left_idx) // 2
            if arr[mid_idx] == target:
                return mid_idx
            elif arr[mid_idx] < target:
                left_idx = mid_idx + 1
            else:
                right_idx = mid_idx - 1

        return -1