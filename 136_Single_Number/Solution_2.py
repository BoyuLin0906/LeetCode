class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 2 * (a + b + c) - (a + a + b + b + c) = c
        nums_2 = sum(set(nums)) * 2
        result = nums_2 - sum(nums)
        return result