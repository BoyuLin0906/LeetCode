class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Runtime: 52 ms, faster than 78.57% of Python3 online submissions for Interleaving String.
        Memory Usage: 13.9 MB, less than 98.22% of Python3 online submissions for Interleaving String.
        """
        # DP (1D)
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
        if s1_len + s2_len != s3_len: return False
        
        if s2_len > s1_len:
            s1_len, s2_len = s2_len, s1_len
            s1, s2 = s2, s1
        
        dp = [True] + [False] * (s2_len)
        for idx in range(1, s2_len + 1):
            dp[idx] = dp[idx-1] and s2[idx-1] == s3[idx-1]

        for s1_idx in range(1, s1_len + 1):
            dp[0] = dp[0] and s1[s1_idx-1] == s3[s1_idx-1]
            # dp[0] => left, d[1] => above
            # dp[1] => left, d[2] => above
            # ...
            for s2_idx in range(1, s2_len + 1):
                selected_s1 ,selected_s2 = False, False
                if s1[s1_idx - 1] == s3[s1_idx - 1 + s2_idx]:
                    selected_s1 = dp[s2_idx]
                if s2[s2_idx - 1] == s3[s1_idx + s2_idx - 1]:
                    selected_s2 = dp[s2_idx - 1]
                dp[s2_idx] = selected_s1 or selected_s2
                
        return dp[s2_len]