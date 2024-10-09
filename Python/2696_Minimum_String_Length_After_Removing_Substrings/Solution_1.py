"""
Runtime 33 ms / Beats 96.89%
Memory 16.58 MB / Beats 41.77%
"""

class Solution:
    def minLength(self, s: str) -> int:
        char_stack = list()
        
        for char in s:
            if len(char_stack) > 0 and ((char_stack[-1] == 'A' and char == 'B') or (char_stack[-1] == 'C' and char == 'D')):
                char_stack.pop(-1)
            else:
                char_stack.append(char)

        return len(char_stack)