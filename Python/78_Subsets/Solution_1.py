class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        nums_length = len(nums)
        result = []
        
        for i in range(0, 1 << nums_length):
            result.append([nums[j] for j in range(nums_length) if (i & (1 << j))])
            
        return result