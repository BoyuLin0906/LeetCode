class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        Runtime: 1992 ms, faster than 23.60% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
        Memory Usage: 36 MB, less than 13.44% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
        """
        # prefix sum + hash
        nums_len = len(nums)
        
        if x > sum(nums): return -1
        elif x == sum(nums): return nums_len
        
        middle_sum = sum(nums) - x
        middle_sum_len = -1
        prefix_sum_dict = dict()
        prefix_sum = 0
        
        for idx in range(nums_len):
            prefix_sum += nums[idx]
            prefix_sum_dict[prefix_sum] = idx
            
            if middle_sum == prefix_sum: 
                middle_sum_len = max(middle_sum_len, idx + 1)
            
            diff_prefix_sum =  prefix_sum - middle_sum
            if diff_prefix_sum in prefix_sum_dict: 
                middle_sum_len = max(middle_sum_len, idx - prefix_sum_dict[diff_prefix_sum])
        
        return -1 if middle_sum_len == -1 else nums_len - middle_sum_len