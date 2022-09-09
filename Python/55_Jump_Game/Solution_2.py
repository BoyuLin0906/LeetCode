class Solution:
    def canJump(self, nums: List[int]) -> bool:
    	"""
    	Runtime: 862 ms, faster than 37.61% of Python3 online submissions for Jump Game.
		Memory Usage: 15.4 MB, less than 18.21% of Python3 online submissions for Jump Game.
    	"""
        nums_len = len(nums)
        goal = nums_len-1
        
        for idx in range(nums_len-2, -1, -1):
            if goal <= nums[idx]+idx:
                goal = idx
                
        return goal == 0