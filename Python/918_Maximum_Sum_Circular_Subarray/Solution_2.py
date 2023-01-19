class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        Runtime 475 ms / Beats 97.19%
        Memory 18.9 MB / Beats 91.66%
        """
        # all negative
        if max(nums) <= 0: return max(nums)

        total = sum(nums)
        min_nums = [num for num in nums]

        # DP
        for idx in range(1, len(nums)):
            if nums[idx-1] > 0:
                nums[idx] += nums[idx-1]
            if min_nums[idx-1] < 0:
                min_nums[idx] += min_nums[idx-1]

        sum_max = max(nums)
        sum_min = min(min_nums)

        return max(sum_max, total-sum_min)