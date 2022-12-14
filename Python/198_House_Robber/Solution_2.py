class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Runtime 30 ms / Beats 96.26%
        Memory 13.9 MB / Beats 66.57%
        """
        nums_len = len(nums)
        prev_thrid_num = 0
        prev_second_num = 0
        prev_num = nums[0]
        curr_num = 0

        for idx in range(1, nums_len):
            curr_num = max(prev_thrid_num, prev_second_num) + nums[idx]
            prev_thrid_num, prev_second_num, prev_num = prev_second_num, prev_num, curr_num

        return max(prev_second_num, prev_num)