class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        count = 0
        sub_string = []

        for i in range(len(s)):
            if s[i] not in sub_string:
                sub_string.append(s[i])
                count += 1
            else:
                for j in range(len(sub_string)):
                    if sub_string[j] == s[i]:
                        sub_string = sub_string[j+1:] + [s[i]]
                        count = len(sub_string)
                        break
                
            if count > max_length:
                max_length = count
        
        return max_length