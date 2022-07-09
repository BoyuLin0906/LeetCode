class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        length = len(prices)
        prev_index, next_index = 0, 1
        max_profit = 0
        
        while prev_index < length and next_index < length:
            if prices[prev_index] <= prices[next_index]:
                max_profit = max(max_profit, prices[next_index]-prices[prev_index])
                next_index += 1
            elif prices[prev_index] > prices[next_index]:
                prev_index +=1
                next_index = prev_index + 1
                
        return max_profit