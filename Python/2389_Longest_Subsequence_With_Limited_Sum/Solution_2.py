class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """
        Runtime 111 ms / Beats 92.82%
        Memory 14.2 MB / Beats 79.61%
        """
        # prefix sum + binary search
        num_len = len(nums)
        query_len = len(queries)

        ans = [num_len] * query_len
        nums.sort()

        for idx in range(1, num_len):
            nums[idx] += nums[idx-1]

        for queried_idx in range(query_len):
            idx = bisect_right(nums, queries[queried_idx])
            ans[queried_idx] = idx

        return ans