class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """
        Runtime: 2161 ms, faster than 77.30% of Python3 online submissions for String Compression II.
        Memory Usage: 368.8 MB, less than 37.42% of Python3 online submissions for String Compression II.
        """
        # DP with cache
        s_len = len(s)
        
        @cache
        def dp(cur_idx, prev_char, prev_cnt, removed_cnt):
            
            if removed_cnt < 0: return inf
            # delete all characters
            # [e.g.] s='aaa', k=3
            if cur_idx == s_len: return 0

            # 1. detele current character
            deleted_value = dp(cur_idx + 1, prev_char, prev_cnt, removed_cnt-1)
            # 2. remain current character
            if s[cur_idx] == prev_char:
                # a. current character is same as previos character
                # [e.g.] aa
                keep_value = dp(cur_idx + 1, prev_char, prev_cnt + 1, removed_cnt)
                # [e.g.] a9 -> a10, a -> a2, a99 -> a100
                if prev_cnt in [1, 9, 99]:  keep_value += 1
            else:
                # b. current character and previos character are different
                # [e.g.] ab
                keep_value = dp(cur_idx + 1, s[cur_idx], 1, removed_cnt) + 1
            
            # get min result
            return min(deleted_value, keep_value)

        return dp(0, '', 0, k)