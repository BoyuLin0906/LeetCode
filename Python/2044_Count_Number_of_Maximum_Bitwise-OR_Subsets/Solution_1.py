"""
Runtime 239 ms / Beats 54.38%
Memory 16.64 MB / Beats 68.18%
"""
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_bitwise_or = 0
        for num in nums:
            max_bitwise_or |= num

        self.total = 0
        self.helper(nums, 0, 0, max_bitwise_or)

        return self.total

    def helper(self, nums, idx, or_num, tagert):

        if idx >= len(nums):
            return
        
        curr_or_num = nums[idx] | or_num
        if curr_or_num == tagert:
            self.total += 1
      
        self.helper(nums, idx+1, or_num, tagert)
        self.helper(nums, idx+1, curr_or_num, tagert)