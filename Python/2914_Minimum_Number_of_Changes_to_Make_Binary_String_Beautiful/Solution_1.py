"""
Runtime 16 ms / Beats 89.19%
Memory 16.80 MB / Beats 99.59%
"""
class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        for idx in range(0, len(s), 2):
            if s[idx] != s[idx+1]:
                count += 1
        return count