class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
		Runtime: 403 ms, faster than 70.63% of Python3 online submissions for 132 Pattern.
		Memory Usage: 32.2 MB, less than 12.38% of Python3 online submissions for 132 Pattern.
        """
        cur_min = nums[0]
        stack = []
        
        for num in nums[1:]:
            while stack and stack[-1][0] <= num: stack.pop()
            if stack and stack[-1][1] < num: return True
            stack.append([num, cur_min])
            cur_min = min(cur_min, num)
            
        return False