class Solution:
    def rob(self, nums: List[int]) -> int:
    	"""
		Runtime 30 ms / Beats 96.26%
		Memory 13.9 MB / Beats 20.34%
    	"""
        nums_len = len(nums)
        dp = [0, 0] + [nums[0]] + (nums_len-1) * [0]

        for idx in range(1, nums_len):
            dp[idx+2] = max(dp[idx], dp[idx-1]) + nums[idx]

        return max(dp[-1], dp[-2])