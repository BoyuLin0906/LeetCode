class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        Runtime 568 ms / Beats 100%
        Memory 28.5 MB / Beats 17.84%
        """
        nums.sort()
        bin_count = "0"
        mod = 10**9 + 7
        left_p, right_p = 0, len(nums)-1

        while left_p <= right_p:
            if nums[left_p] + nums[right_p] > target:
                bin_count += "0"
                right_p -= 1
            else:
                bin_count += "1"
                left_p += 1
            
        return int(bin_count, 2) % mod