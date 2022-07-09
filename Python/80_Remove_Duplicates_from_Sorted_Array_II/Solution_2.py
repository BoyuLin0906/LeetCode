class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        result_pointer = 1
        count, num = 1, nums[0]
        
        for i in range(1, len(nums)):
            if num != nums[i]:
                count = 0
                num = nums[i]
                
            if num == nums[i] and count < 2:
                nums[result_pointer] = num
                result_pointer += 1
                count += 1
        
        return result_pointer