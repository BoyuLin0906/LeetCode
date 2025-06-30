class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        Runtime 56 ms / Beats 19.41%
        Memory 18.70 MB / Beats 99.67%
        """
        nums.sort()
        max_len = 0
        prev_idx = 0

        for idx in range(1, len(nums)):
            while nums[idx] - nums[prev_idx] > 1:
                prev_idx += 1
            if nums[idx] - nums[prev_idx] == 1:
                max_len = max(max_len, idx - prev_idx + 1)

        return max_len