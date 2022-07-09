class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Runtime: 96 ms, faster than 14.96% of Python3 online submissions for Interleaving String.
        Memory Usage: 14.1 MB, less than 73.22% of Python3 online submissions for Interleaving String.
        """
        # DP (2D)
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
        if s1_len + s2_len != s3_len: return False
        
        dp = [[False] * (s1_len + 1) for _ in range(s2_len + 1)]       
        dp[0][0] = True
        
        for idx in range(1, s1_len + 1):
            dp[0][idx] = dp[0][idx-1] and s1[idx-1] == s3[idx-1]
        
        for idx in range(1, s2_len + 1):
            dp[idx][0] = dp[idx-1][0] and s2[idx-1] == s3[idx-1]
        
        for s1_idx in range(1, s1_len + 1):
            for s2_idx in range(1, s2_len + 1):
                if s1[s1_idx - 1] == s3[s1_idx - 1 + s2_idx]:
                    dp[s2_idx][s1_idx] |= dp[s2_idx][s1_idx - 1]
                if s2[s2_idx - 1] == s3[s1_idx + s2_idx - 1]:
                    dp[s2_idx][s1_idx] |= dp[s2_idx - 1][s1_idx]
                    
        return dp[s2_len][s1_len]