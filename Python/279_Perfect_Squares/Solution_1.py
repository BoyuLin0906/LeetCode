from math import isqrt

class Solution:
    def numSquares(self, n: int, dp = [0]) -> int:
    	# the dp is reused for running test
    	# record the same value in dp
        for i in range(len(dp), n+1):
            if len(dp) == i: dp.append(inf)
            for j in range(1, isqrt(i)+1):
                dp[i] = min(dp[i], dp[i - j**2] + 1)
                
        return dp[n]