class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_length = len(s)
        longest_string = ''
        
        def check_palindromic(left, right):
            # middle to left and right
            while left >= 0 and right < str_length and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
                  
        for i in range(str_length):
            odd_str = check_palindromic(i,i)
            even_str = check_palindromic(i,i+1)
            longest_string = max(longest_string, odd_str,even_str, key=lambda x: len(x))
                
        return longest_string