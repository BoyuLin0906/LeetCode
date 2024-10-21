"""
Runtime 479 ms / Beats 5.27%
Memory 35.07 MB / Beats 39.28%
"""
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        nums_len = len(nums)
        tagert_remainder = 0

        for num in nums:
            tagert_remainder = (tagert_remainder + num) % p

        if tagert_remainder == 0:
            return 0

        mod_map = {0 : -1}
        current_sum = 0
        min_len = nums_len

        for idx in range(nums_len):
            current_sum = (current_sum + nums[idx]) % p
            need_num = (current_sum - tagert_remainder + p) % p

            if need_num in mod_map:
                min_len = min(min_len, idx - mod_map[need_num])

            mod_map[current_sum] = idx

        if min_len == nums_len:
            return -1
        return min_len