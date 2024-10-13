"""
Runtime 50 ms / Beats 83.33%
Memory 16.57 MB / Beats 70.30%
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sorted_nums = sorted(nums)
        nums_smaller_amount = dict()
        for idx in range(len(nums)):
            if not sorted_nums[idx] in nums_smaller_amount:
                nums_smaller_amount[sorted_nums[idx]] = idx
        
        smaller_oupout = [0] * len(nums)
        for idx in range(len(nums)):
            num = nums[idx]
            smaller_oupout[idx] = nums_smaller_amount[num]
            
        return smaller_oupout