"""
Runtime 46 ms / Beats 75.00%
Memory 32.21 MB / Beats 88.95%
"""
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        nums_len = len(nums)
        maximum_xor_num = (2 ** maximumBit) - 1

        xor_product = nums[0]
        for idx in range(1, nums_len):
            xor_product = xor_product ^ nums[idx]

        res = []
        for idx in range(nums_len-1, -1, -1):
            ans = maximum_xor_num ^ xor_product
            res.append(ans)
            xor_product = xor_product ^ nums[idx]

        return res