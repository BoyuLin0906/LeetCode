"""
Runtime 313 ms / Beats 98.75%
Memory 26.78 MB / Beats 81.82%
"""

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        largest_combination = 0

        mask = 1
        for idx in range(24):
            count = 0
            for candidate in candidates:
                if candidate & mask:
                    count += 1

            largest_combination = max(largest_combination, count)
            mask = mask << 1

        return largest_combination