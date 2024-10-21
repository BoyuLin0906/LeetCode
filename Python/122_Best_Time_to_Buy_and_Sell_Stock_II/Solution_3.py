'''
Runtime 59 ms / Beats 48.60%
Memory 17.96 MB / Beats 19.50%
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        if n == 0:
            return 0

        not_hold_stock = 0
        hold_stock = -prices[0]

        for i in range(1, n):
            next_not_hold_stock = max(not_hold_stock, hold_stock + prices[i])
            next_hold_stock = max(hold_stock, not_hold_stock - prices[i])
            not_hold_stock = next_not_hold_stock
            hold_stock = next_hold_stock
        
        return not_hold_stock