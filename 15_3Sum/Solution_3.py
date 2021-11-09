class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # advance solution 1
        length = len(nums)
        if length < 3: return []
        
        result_set = set()
        nums.sort()
        
        for i in range(length):
            if nums[i] > 0: break
            if i >= 1 and nums[i] == nums[i-1]: continue
                
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