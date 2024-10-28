"""
Runtime 92 ms / Beats 78.13%
Memory 22.86 MB / Beats 97.89%
"""

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        hold_stock = -prices[0]
        unhold_stock = 0

        for price in prices:
            curr_hold_stock = max(hold_stock, unhold_stock - price)
            curr_unhold_stock = max(unhold_stock, hold_stock + price - fee)
            
            hold_stock = curr_hold_stock
            unhold_stock = curr_unhold_stock

        return unhold_stock
