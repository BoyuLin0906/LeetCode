class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        Runtime 48 ms / Beats 91.79%
        Memory 14 MB / Beats 99.11%
        """
        # two counter
        left_count = right_count = 0
        s_len = len(s)
        max_len = 0

        # left to right
        for idx in range(s_len):
            if s[idx] == '(': left_count += 1
            elif s[idx] == ')': right_count += 1
            
            if left_count == right_count:
                max_len = max(max_len, left_count*2)
            elif right_count > left_count:
                left_count = right_count = 0

        left_count = right_count = 0
        # right to left
        for idx in range(s_len-1, -1, -1):
            if s[idx] == '(': left_count += 1
            elif s[idx] == ')': right_count += 1
            
            if left_count == right_count:
                max_len = max(max_len, left_count*2)
            elif right_count < left_count:
                left_count = right_count = 0

        return max_len