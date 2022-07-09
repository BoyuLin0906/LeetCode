class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        Runtime: 3104 ms, faster than 82.53% of Python3 online submissions for Ones and Zeroes.
        Memory Usage: 14.2 MB, less than 81.02% of Python3 online submissions for Ones and Zeroes.
        """
        # Knapsack Problem
        # DP (0/1 Knapsack Problem)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for str in strs:
            zero_count, one_count = str.count('0'), str.count('1')
            
            for zero_idx in range(m, zero_count - 1, -1):
                for one_idx in range(n, one_count - 1, -1):
                    dp[one_idx][zero_idx] = max(dp[one_idx][zero_idx], dp[one_idx - one_count][zero_idx - zero_count] + 1)
            

        return dp[n][m]