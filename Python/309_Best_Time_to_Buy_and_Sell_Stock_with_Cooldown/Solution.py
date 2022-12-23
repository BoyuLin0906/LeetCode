class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Runtime 38 ms / Beats 97.56%
        Memory 14.2 MB / Beats 65.62%
        """
        sold = 0
        held = -prices[0]
        reset = 0

        for idx in range(1, len(prices)):
            prev_sold = sold
            sold = held + prices[idx]
            held = max(held, reset - prices[idx])
            reset = max(reset, prev_sold)

        return max(sold, reset)