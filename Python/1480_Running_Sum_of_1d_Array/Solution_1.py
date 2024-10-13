"""
Runtime 42 ms / Beats 53.97%
Memory 16.63 MB / Beats 75.11%
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]

        return nums