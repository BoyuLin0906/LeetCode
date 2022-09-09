class Solution:
    def canJump(self, nums: List[int]) -> bool:
    	"""
		Runtime: 4525 ms, faster than 8.71% of Python3 online submissions for Jump Game.
		Memory Usage: 15.3 MB, less than 49.05% of Python3 online submissions for Jump Game.
    	"""
        nums_len = len(nums)
        dp = [False] * (nums_len-1) + [True]
        
        for idx in range(nums_len-2, -1, -1):
            if any(dp[idx+1:nums[idx]+idx+1]):
                dp[idx] = True
                    
        return dp[0]