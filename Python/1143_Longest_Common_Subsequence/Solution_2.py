class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Runtime 451 ms / Beats 74.9%
        Memory 13.9 MB / Beats 93.49%
        """
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        t1_len, t2_len = len(text1), len(text2)
        dp = [[0] * (t1_len + 1) for _ in range(2)]

        for t2_idx in range(t2_len):
            for t1_idx in range(t1_len):
                t2_idx_dp = t2_idx % 2
                
                value = dp[t2_idx_dp][t1_idx] + 1
                if text1[t1_idx] != text2[t2_idx]:
                    # from left and top 
                    value = max(dp[1-t2_idx_dp][t1_idx], dp[t2_idx_dp][t1_idx+1])
                dp[1-t2_idx_dp][t1_idx+1] = value

        return dp[t2_len%2][-1]