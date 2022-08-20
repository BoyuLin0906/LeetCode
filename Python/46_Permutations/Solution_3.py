class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Runtime: 43 ms, faster than 91.49% of Python3 online submissions for Permutations.
        Memory Usage: 14.1 MB, less than 22.97% of Python3 online submissions for Permutations.
        """
        # backtracking + swap
        nums_len = len(nums)
        if nums_len == 1: return [nums]
        
        results = []
        
        def backtrack(idx):
            if idx == nums_len:
                results.append(nums.copy())
            else:
                for idx_n in range(idx, nums_len):
                    nums[idx], nums[idx_n] = nums[idx_n], nums[idx]
                    backtrack(idx+1)
                    nums[idx_n], nums[idx] = nums[idx], nums[idx_n]
        
        backtrack(0)
        
        return results