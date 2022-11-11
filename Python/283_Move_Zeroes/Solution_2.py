class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Runtime 169 ms / Beats 94.95%
		Memory 15.7 MB / Beats 17.31%
        """
        left_idx = 0

        for right_idx in range(len(nums)):
            if nums[right_idx] != 0:
               nums[right_idx], nums[left_idx] = nums[left_idx], nums[right_idx]
               left_idx += 1