"""
Runtime 759 ms / Beats 37.85%
Memory 26.86 MB / Beats 79.81%
"""

from collections import defaultdict

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        total = 0
        mapping = defaultdict(int)

        left_idx = 0
        for idx in range(len(nums)):
            num = nums[idx]
            mapping[num] += 1

            while max(mapping.keys()) - min(mapping.keys()) > 2:
                mapping[nums[left_idx]] -= 1
                if mapping[nums[left_idx]] == 0:
                    del mapping[nums[left_idx]]
                left_idx += 1

            total += idx - left_idx + 1

        return total