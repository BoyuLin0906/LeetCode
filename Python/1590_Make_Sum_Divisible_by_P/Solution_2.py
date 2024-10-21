class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # sum[i:j] = prefix_sum[j] - prefix_sum[i]
        nums_len = len(nums)

        tagert_remainder = sum(nums) % p
        if tagert_remainder == 0:
            return 0
        
        curr_sum = 0
        min_len = nums_len
        prefix_sum_to_idx = {0 : -1}
        for idx in range(nums_len):
            if nums[idx] % p == tagert_remainder:
                return 1
            curr_sum = (curr_sum + nums[idx]) % p
            need_curr_sum = (curr_sum - tagert_remainder + p) % p
            
            if need_curr_sum in prefix_sum_to_idx:
                min_len = min(min_len, idx - prefix_sum_to_idx[need_curr_sum])

            prefix_sum_to_idx[curr_sum] = idx

        if min_len == nums_len:
            return -1
        return min_len