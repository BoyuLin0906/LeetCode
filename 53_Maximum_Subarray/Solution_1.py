class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        table = [nums[0]] + [0] * (len(nums)-1)
        for i in range(1, len(nums)):
            table[i] = max(nums[i] + table[i-1], nums[i]) 
        return max(table)