"""
Runtime 630 ms / Beats 9.01%
Memory 33.70 MB / Beats 9.48%
"""

from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        nums_len = len(nums)
        
        left_counter = Counter()
        right_counter = Counter(nums)
        dominant_num = right_counter.most_common()[0][0]

        for idx in range(nums_len):
            left_counter[nums[idx]] += 1
            right_counter[nums[idx]] -= 1

            if dominant_num != nums[idx]:
                continue

            left_dominant_count = left_counter[dominant_num]
            right_dominant_count = right_counter[dominant_num]
            if right_dominant_count == 0:
                break

            if self.is_dominant(idx+1, left_dominant_count) and self.is_dominant(nums_len-(idx+1), right_dominant_count):
                return idx

        return -1

    def is_dominant(self, threshold, dominant_count):
        if dominant_count * 2 > threshold:
            return True
        return False