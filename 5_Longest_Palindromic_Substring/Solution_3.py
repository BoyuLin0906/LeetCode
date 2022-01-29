class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_length = len(s)
        
        # initialization
        longest_string = s[0]
        dp = [[False] * str_length for _ in range(str_length)]
        for i in range(str_length): dp[i][i] = True
            
        # dynamic programming
        for right in range(str_length):
            for left in range(right):
                if s[right] == s[left] and (dp[left+1][right-1] or left + 1 == right):
                    dp[left][right] = True
                    if right - left + 1 > len(longest_string): longest_string = s[left:right+1]
                    
        return longest_string