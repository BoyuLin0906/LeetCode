class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_value = max_value = nums[0]
        for i in range(1, len(nums)):
            cur_value = max(nums[i], cur_value + nums[i])
            max_value = max(cur_value, max_value)
        return max_value