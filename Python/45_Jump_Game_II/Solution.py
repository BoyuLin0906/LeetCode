class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Runtime: 213 ms, faster than 61.74% of Python3 online submissions for Jump Game II.
        Memory Usage: 15 MB, less than 90.64% of Python3 online submissions for Jump Game II.
        """
        nums_len = len(nums)
        if nums_len == 1: return 0
        
        goal = last_pos = count = 0
        for idx in range(nums_len):
            step = nums[idx]
            goal = max(goal, idx+step)
            
            if idx == last_pos:
                last_pos = goal
                count += 1
                if goal >= nums_len-1:
                    return count
                
        return count