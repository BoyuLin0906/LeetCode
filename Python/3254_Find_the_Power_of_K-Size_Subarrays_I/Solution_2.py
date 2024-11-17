class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        consecutive_count = 1
        res = [-1] * (len(nums) - k + 1)

        for idx in range(1, len(nums)):
            if nums[idx-1] + 1 == nums[idx]:
                consecutive_count += 1
            else:
                consecutive_count = 1

            if consecutive_count >= k:
                res[idx-k+1] = nums[idx]

        return res