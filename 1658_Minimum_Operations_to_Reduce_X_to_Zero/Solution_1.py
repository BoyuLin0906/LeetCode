class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        Runtime: 1571 ms, faster than 56.37% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
        Memory Usage: 27.9 MB, less than 82.08% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
        """
        # sliding window + prefix sum 
        nums_len = len(nums)
        if x > sum(nums): return -1
        elif x == sum(nums): return nums_len
        
        middle_sum = sum(nums) - x
        start_idx = 0
        current_sum = 0
        middle_sum_len = -1
        
        for end_idx in range(nums_len):
            current_sum += nums[end_idx]
            while end_idx >= start_idx and current_sum > middle_sum:
                current_sum -= nums[start_idx]
                start_idx += 1
                
            if current_sum == middle_sum:
                middle_sum_len = max(middle_sum_len, end_idx - start_idx + 1)
        
        return -1 if middle_sum_len == -1 else nums_len - middle_sum_len