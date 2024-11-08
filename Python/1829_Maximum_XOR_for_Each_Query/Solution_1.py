"""
Runtime 52 ms / Beats 65.18%
Memory 35.24 MB / Beats 28.78%
"""
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        nums_len = len(nums)
        maximum_xor_num = (2 ** maximumBit) - 1
        
        prefix_sum = [0] * nums_len
        prefix_sum[0] = nums[0]

        for idx in range(1, nums_len):
            prefix_sum[idx] = prefix_sum[idx-1] ^ nums[idx]

        res = []
        for idx in range(nums_len-1, -1, -1):
            ans = maximum_xor_num ^ prefix_sum[idx]
            res.append(ans)

        return res