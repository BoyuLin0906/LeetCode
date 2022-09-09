class Solution:
    def canJump(self, nums):
    	"""
    	Runtime: 657 ms, faster than 67.80% of Python3 online submissions for Jump Game.
		Memory Usage: 15.1 MB, less than 81.45% of Python3 online submissions for Jump Game.
    	"""
        goal = 0
        
        for idx, step in enumerate(nums):
            if idx > goal: return False
            goal = max(goal, idx+step)
            
        return True