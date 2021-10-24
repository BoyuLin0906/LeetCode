class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        char_table = {}
        
        for right in range(len(s)):
            # new char
            if s[right] not in char_table:
                max_length = max(max_length, right - left + 1)
            # existed char
            else:
                if char_table[s[right]] < left:
                    max_length = max(max_length, right - left + 1)
                # Move left pointer to the next position of the repeated char
                else:
                    left = char_table[s[right]] + 1
            # update char and thier position
            char_table[s[right]] = right
        return max_length     