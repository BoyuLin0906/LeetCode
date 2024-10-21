"""
Runtime 135 ms / Beats 93.05%
Memory 16.61 MB / Beats 19.96%
"""
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.max_length = 0
        self.substring = dict()
        self.helper(s, 0, self.substring)
        
        return self.max_length

    def helper(self, string, idx, substring):
        if idx >= len(string):
            self.max_length = max(len(substring), self.max_length)
            return

        for right_idx in range(idx+1, len(string)+1):
            sub_str = string[idx:right_idx]
            if sub_str in substring:
                continue
            
            substring[sub_str] = True
            self.helper(string, right_idx, substring)
            del substring[sub_str]