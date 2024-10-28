"""
Runtime 115 ms / Beats 59.46%
Memory 33.82 MB / Beats 48.00%
"""

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        unique_numbers = set(nums)
        max_longest_square = 1

        for num in nums:

            current_num = num
            currect_count = 0
            while current_num in unique_numbers:
                
                currect_count += 1
                current_num = current_num ** 2
                if current_num > 10**5:
                    break

            max_longest_square = max(max_longest_square, currect_count)

        if max_longest_square == 1:
            return -1

        return max_longest_square