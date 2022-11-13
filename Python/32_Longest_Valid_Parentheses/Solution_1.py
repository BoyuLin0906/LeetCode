class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        Runtime 45 ms / Beats 95.1%
        Memory 14.6 MB / Beats 60.13%
        """
        # stack
        stack = [-1]
        max_len = 0
        for idx in range(len(s)):
            if s[idx] == '(':
                stack.append(idx)
            else:
                stack.pop()
                if not stack:
                    stack.append(idx)
                else:
                    max_len = max(max_len, idx-stack[-1])
        return max_len