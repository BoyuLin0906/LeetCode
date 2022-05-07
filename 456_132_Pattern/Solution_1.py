class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        Runtime: 501 ms, faster than 40.93% of Python3 online submissions for 132 Pattern.
        Memory Usage: 32.1 MB, less than 67.82% of Python3 online submissions for 132 Pattern.
        """
        if len(nums) < 3: return False
        
        mono_stack = []
        tail_num = -math.inf
        
        for num in nums[::-1]:
            # check if head number is smaller than tail number
            if num < tail_num: return True
            
            # 1. find the number as middle number
            # 2. find out the biggest tail number which is not bigger than middle number 
            while mono_stack and mono_stack[-1] < num:
                tail_num = mono_stack.pop()
            mono_stack.append(num)
            
        return False