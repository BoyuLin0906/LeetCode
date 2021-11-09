class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result_set = set()
        nums.sort()
        length = len(nums)
        
        for i in range(length):
            left_p, right_p = i+1, length-1
            
            while left_p < right_p:
                
                tmp_sum = nums[i] + nums[left_p] + nums[right_p]
                if tmp_sum == 0:
                    result_set.add((nums[i], nums[left_p], nums[right_p]))
                    left_p += 1   
                    right_p -= 1
                elif tmp_sum > 0:
                    right_p -= 1
                else:
                    left_p += 1   
        
        return [list(i) for i in result_set]