class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_2 = sum(set(nums)) * 3
        result = (nums_2 - sum(nums)) // 2
        return result