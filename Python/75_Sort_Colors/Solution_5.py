class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        left_index, right_index = 0, len(nums)-1
        pointer = 0
        
        while pointer <= right_index:
            if nums[pointer] == 0:
                nums[left_index], nums[pointer] = nums[pointer], nums[left_index]
                left_index += 1
                pointer += 1
            elif nums[pointer] == 1:
                pointer += 1
            else:
                nums[right_index], nums[pointer] = nums[pointer], nums[right_index]
                right_index -= 1