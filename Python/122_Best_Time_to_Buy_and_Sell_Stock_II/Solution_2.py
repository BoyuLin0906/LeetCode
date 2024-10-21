'''
Runtime 52 ms / Beats 85.59%
Memory 17.86 MB / Beats 69.99%
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        for idx in range(1, len(prices)):
            diff = prices[idx]-prices[idx-1]
            if diff > 0:
                max_profit += diff

        return max_profit