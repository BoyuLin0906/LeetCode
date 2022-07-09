class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR
        result = 0
        for x in nums:
            result ^= x
            
        return result