class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # list
        max_length = 0
        sub_string = []
        pointer = 0
        str_len = len(s)
        
        while pointer < str_len:
            if s[pointer] in sub_string:
                sub_string.pop(0)
            else:
                sub_string.append(s[pointer])
                pointer += 1
                max_length = max(len(sub_string), max_length)
            
        return max_length