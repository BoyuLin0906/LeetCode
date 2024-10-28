"""
Runtime 129 ms / Beats 48.65%
Memory 37.14 MB / Beats 16.00%
"""

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()

        nums_dict = dict()
        for num in nums:
            nums_dict[num] = 1

        for num in nums:
            square_num = num * num
            if square_num in nums_dict:
                nums_dict[square_num] = nums_dict[num] + 1
        
        max_longest_square = 1
        for count in nums_dict.values():
            max_longest_square = max(max_longest_square, count)

        if max_longest_square == 1:
            return -1

        return max_longest_square