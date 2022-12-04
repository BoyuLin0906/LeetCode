class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0

        right_sum = sum(nums)
        left_sum = 0
        num_len = len(nums)
        index = 0
        min_sum = inf

        for idx in range(num_len):
            left_sum += nums[idx]
            right_sum -= nums[idx]
            diff = left_sum//(idx+1)

            if num_len-idx-1 != 0:
                diff = abs(diff - right_sum//(num_len-idx-1))
            if diff < min_sum:
                min_sum = diff
                index = idx

        return index