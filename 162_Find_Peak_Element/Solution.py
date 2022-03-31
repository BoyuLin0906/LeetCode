class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        nums_len = len(nums)-1
        left_idx, right_idx = 0, nums_len
        mid_idx = 0
        
        while left_idx <= right_idx:

            mid_idx = (left_idx + right_idx) // 2
            if (mid_idx == 0 or nums[mid_idx] >= nums[mid_idx-1]) and (mid_idx == nums_len or nums[mid_idx] >= nums[mid_idx+1]):
                return mid_idx
            elif mid_idx > 0 and nums[mid_idx] < nums[mid_idx-1]:
                right_idx = mid_idx - 1
            else:
                left_idx = mid_idx + 1

        return mid_idx