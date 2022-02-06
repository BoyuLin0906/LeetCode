class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # allocate extra space for another array (not)
        temp_nums = [nums[0]]
        head_num = nums[0]
        count = 1
        
        for i in range(1, len(nums)):
            if head_num == nums[i] and count < 2:
                temp_nums.append(head_num)
                count += 1
            elif head_num != nums[i]:   
                head_num = nums[i]
                temp_nums.append(head_num)
                count = 1
                
        result_nums_length = len(temp_nums)
        for i in range(result_nums_length): nums[i] = temp_nums[i]
        
        return result_nums_length