class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_length = len(s)
        longest_string = ''

        for i in range(str_length):
            sub_string = ''
            for j in range(i, str_length):
                sub_string += s[j]
                if sub_string == sub_string[::-1] and len(sub_string) > len(longest_string):
                    longest_string = sub_string
                    
        return longest_string

# Time Limit Exceeded