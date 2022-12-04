class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        """
        Runtime 952 ms / Beats 98.83%
        Memory 26.1 MB / Beats 20.66%
        """
        if len(nums) <= 1: return 0

        nums_sum, num_len = 0, len(nums)
        for idx in range(1, num_len):
            nums[idx] += nums[idx-1]

        min_sum = inf
        count, index = 1, 0
        for num in nums:
            diff = num//count
            if count != num_len:
                diff = abs(diff - ((nums[-1]-num)//(num_len-count)))
            if min_sum > diff:
                min_sum = diff
                index = count-1
            count += 1

        return index