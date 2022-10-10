class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """
        Runtime: 16 ms, faster than 99.96% of Python3 online submissions for Break a Palindrome.
        Memory Usage: 13.8 MB, less than 96.39% of Python3 online submissions for Break a Palindrome.
        """
        str_len = len(palindrome)
        if str_len == 1: return ""
            
        half_str_len = (str_len // 2)
        palindrome = list(palindrome)
        
        # ex: abcba, cdc 
        for idx in range(half_str_len):
            if palindrome[idx] != 'a': 
                palindrome[idx] = 'a'
                return ''.join(palindrome)
        
        # ex: aaaaa, aaabaaa, aa 
        palindrome[-1] = 'b'
        return ''.join(palindrome)