class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Runtime: 48 ms, faster than 82.01% of Python3 online submissions for Permutations.
        Memory Usage: 14 MB, less than 84.57% of Python3 online submissions for Permutations.
        """
        # dfs + for loop
        nums_len = len(nums)
        if nums_len == 1: return [nums]
        
        queue = []
        results = []
        
        for num in nums:
            queue.append([num])
        
        while queue:
            result = queue.pop()
            if nums_len == len(result):
                results.append(result)
            else:  
                for num in nums:
                    if not num in result:
                        queue.append(result + [num])
        
        return results