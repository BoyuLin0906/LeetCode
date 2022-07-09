class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Runtime: 58 ms, faster than 65.24% of Python3 online submissions for Interleaving String.
        Memory Usage: 14.9 MB, less than 38.00% of Python3 online submissions for Interleaving String.
        """
        # dfs + cache
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)
        if s1_len + s2_len != s3_len: return False
        
        @cache
        def dfs(s1_idx, s2_idx, s3_idx):
            if s1_idx == s1_len:
                return s2[s2_idx:] == s3[s3_idx:]
            elif s2_idx == s2_len:
                return s1[s1_idx:] == s3[s3_idx:]
            elif s1[s1_idx] == s3[s3_idx] and dfs(s1_idx+1, s2_idx, s3_idx+1):
                return True
            elif s2[s2_idx] == s3[s3_idx] and dfs(s1_idx, s2_idx+1, s3_idx+1):
                return True
            return False
        
        return dfs(0,0,0)