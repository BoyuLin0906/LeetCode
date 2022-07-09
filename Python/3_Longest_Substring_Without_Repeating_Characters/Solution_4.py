class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        sub_string = []
        left, right = 0, 0
        str_len = len(s)
        
        while right < str_len:
            if s[right] in sub_string:
                sub_string.pop(0)
                left += 1
            else:
                sub_string.append(s[right])
                right += 1
                max_length = max(right-left, max_length)
            
        return max_length