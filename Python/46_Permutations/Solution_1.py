class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Runtime: 50 ms, faster than 77.81% of Python3 online submissions for Permutations.
        Memory Usage: 14.2 MB, less than 22.97% of Python3 online submissions for Permutations.
        """
        # dfs + resursion
        nums_len = len(nums)
        if nums_len == 1: return [nums]
        
        results = list()
        
        def dfs(result):
            if nums_len == len(result):
                results.append(result)
            else:  
                for num in nums:
                    if not num in result:
                        dfs(result + [num])
            
        dfs([])
        return results