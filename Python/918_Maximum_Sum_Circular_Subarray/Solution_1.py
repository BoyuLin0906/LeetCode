class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        Runtime 500 ms / Beats 94.14%
        Memory 19 MB / Beats 43.2%
        """
        # all negative
        if max(nums) <= 0: return max(nums)

        global_max = local_max = 0
        global_min = local_min = 0

        # Kadane’s Algorithm
        for num in nums:
            local_max = max(num, local_max + num)
            global_max = max(global_max, local_max)
            local_min = min(num, local_min + num)
            global_min = min(global_min, local_min)
           
        return max(global_max, sum(nums)-global_min)