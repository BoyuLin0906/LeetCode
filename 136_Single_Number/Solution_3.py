class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    	# not a good solution
        for num in nums:
            if nums.count(num) == 1: return num