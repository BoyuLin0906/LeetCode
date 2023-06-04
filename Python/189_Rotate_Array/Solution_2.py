class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Runtime 215 ms / Beats 82.34%
		Memory 27.8 MB / Beats 45.30%
        """
        nums_len = len(nums)
        k = k % nums_len

        nums[:nums_len-k] = nums[:nums_len-k][::-1]
        nums[nums_len-k:] = nums[nums_len-k:][::-1]
        nums[:] = nums[::-1]