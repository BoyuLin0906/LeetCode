class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        _max_profit = 0
        buy_price = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
            else:
                _max_profit = max(_max_profit, prices[i]-buy_price)
        
        return _max_profit