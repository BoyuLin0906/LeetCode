"""
Runtime 705 ms / Beats 17.50%
Memory 26.76 MB / Beats 81.82%
"""

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        counter = [0] * 25

        for candidate in candidates:
            for idx in range(25):
                temp = candidate & (1 << idx)
                if temp > 0:
                    counter[idx] += 1
        
        largest_combination = 0
        for idx in range(25):
            largest_combination = max(largest_combination, counter[idx])

        return largest_combination