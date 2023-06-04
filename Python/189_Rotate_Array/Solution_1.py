class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Runtime 242 ms / Beats 28.15%
        Memory 27.7 MB / Beats 64.37%
        """

        def reverse(start_idx, end_idx):
            while start_idx < end_idx:
                nums[start_idx], nums[end_idx] = nums[end_idx], nums[start_idx]
                start_idx += 1
                end_idx -= 1

        nums_len = len(nums)
        k = k % nums_len
        reverse(0, nums_len-1)
        reverse(0, k-1)
        reverse(k, nums_len-1)