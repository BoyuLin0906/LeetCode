class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0 
        
        count = 0
        elements_num = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                count  += 1
            else:
                nums[i+1-count] = nums[i+1]
                elements_num += 1
        return elements_num