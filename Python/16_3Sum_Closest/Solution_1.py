class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        length = len(nums)
        if length < 3: return sum(nums)
        
        nums.sort()
        closet_sum, closet_diff = 0, 100000
        
        for i in range(length-2):
            left_p, right_p = i+1, length-1
            while left_p < right_p:
                
                tmp_sum = nums[i] + nums[left_p] + nums[right_p]
                if tmp_sum == target: return tmp_sum
                
                dist_len = abs(tmp_sum - target)
                if dist_len < closet_diff:
                    closet_diff = dist_len
                    closet_sum = tmp_sum
                
                if tmp_sum > target: right_p -= 1
                else: left_p += 1   
        
        return closet_sum