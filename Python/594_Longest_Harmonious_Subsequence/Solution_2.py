class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        Runtime 15 ms / Beats 96.80%
        Memory 19.06 MB / Beats 72.21%
        """
        counter = Counter(nums)
        max_len = 0

        for num in counter:
            if num + 1 in counter:
                max_len = max(max_len, counter[num]+counter[num+1])

        return max_len