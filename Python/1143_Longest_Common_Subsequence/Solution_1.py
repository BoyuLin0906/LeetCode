class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Runtime 458 ms / Beats 72.86%
        Memory 21.8 MB / Beats 88.19%
        """
        t1_len, t2_len = len(text1), len(text2)
        dp = [[0] * (t2_len + 1) for _ in range(t1_len + 1)]

        for t1_idx in range(t1_len):
            for t2_idx in range(t2_len):
                value = dp[t1_idx][t2_idx] + 1
                if text1[t1_idx] != text2[t2_idx]:
                    # from left and top 
                    value = max(dp[t1_idx+1][t2_idx], dp[t1_idx][t2_idx+1])
                dp[t1_idx+1][t2_idx+1] = value

        return dp[-1][-1]