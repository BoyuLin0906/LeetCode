class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        Runtime 36 ms / Beats 44.65%
        Memory 19.18 MB / Beats 46.65%
        """
        counter = Counter(nums)
        nums = sorted(counter.keys())
        max_len = 0

        for idx in range(1, len(nums)):
            if nums[idx] - nums[idx-1] == 1:
                max_len = max(max_len, counter[nums[idx]]+counter[nums[idx-1]])

        return max_len