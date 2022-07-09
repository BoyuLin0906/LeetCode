class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Dynamic programming
        length = len(prices)
        dp_table = [0] * length
        # (min price, max profit)
        dp_table[0] = (prices[0], 0)
        
        for i in range(1, len(prices)):
            min_price, max_profit = dp_table[i-1]
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i]-min_price)
            dp_table[i] = (min_price, max_profit)
            
        return dp_table[length-1][1]