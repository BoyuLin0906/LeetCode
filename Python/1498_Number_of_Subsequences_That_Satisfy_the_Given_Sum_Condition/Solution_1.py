class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        Runtime 7869 ms / Beats 52.77%
        Memory 29.1 MB / Beats 14.20%
        """
        nums.sort()
        count = 0
        mod = 10**9 + 7
        left_p, right_p = 0, len(nums)-1

        while left_p <= right_p:
            if nums[left_p] + nums[right_p] > target:
                right_p -= 1
            else:
                diff = right_p - left_p
                count += 2 ** (diff)
                left_p += 1
            
        return count % mod