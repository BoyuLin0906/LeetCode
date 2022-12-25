class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """
        Runtime 405 ms / Beats 39.90%
        Memory 14.1 MB / Beats 79.61%
        """
        # prefix sum
        num_len = len(nums)
        query_len = len(queries)

        ans = [num_len] * query_len
        nums.sort()

        for idx in range(1, num_len):
            nums[idx] += nums[idx-1]

        for queried_idx in range(query_len):
            for num_idx in range(num_len):
                if nums[num_idx] == queries[queried_idx]:
                    ans[queried_idx] = num_idx+1
                    break
                elif nums[num_idx] > queries[queried_idx]:
                    ans[queried_idx] = num_idx
                    break

        return ans