'''
Runtime 60 ms / Beats 41.31%
Memory 19.71 MB / Beats 5.46%
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        if n == 0:
            return 0

        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        
        return dp[n-1][0]