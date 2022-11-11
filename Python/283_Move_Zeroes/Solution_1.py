class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Runtime 180 ms / Beats 88.44%
        Memory 15.5 MB / Beats 96.98%
        """

        idx = count = 0
        nums_len = len(nums)

        while count < nums_len:
            if nums[idx] == 0:
                nums.append(nums.pop(idx))
            else:
                idx += 1
            count += 1