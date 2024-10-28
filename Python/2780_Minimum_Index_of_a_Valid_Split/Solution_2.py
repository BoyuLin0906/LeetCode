"""
Runtime 528 ms / Beats 55.92%
Memory 31.31 MB / Beats 59.72%
"""

from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        nums_len = len(nums)
        
        counter = Counter(nums)
        dominant_num, right_dominant_count = counter.most_common()[0]
        left_dominant_count = 0

        for idx in range(nums_len):
            if dominant_num != nums[idx]:
                continue
            
            left_dominant_count += 1
            right_dominant_count -= 1

            if self.is_dominant(idx+1, left_dominant_count) and self.is_dominant(nums_len-(idx+1), right_dominant_count):
                return idx

        return -1

    def is_dominant(self, threshold, dominant_count):
        if dominant_count * 2 > threshold:
            return True
        return False