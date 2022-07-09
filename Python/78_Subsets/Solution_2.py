class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = [[]]
        for num in sorted(nums):
            result += [ item + [num] for item in result]
        return result