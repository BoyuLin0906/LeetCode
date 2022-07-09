class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
		Runtime: 1627 ms, faster than 70.37% of Python3 online submissions for Coin Change.
		Memory Usage: 14.2 MB, less than 46.46% of Python3 online submissions for Coin Change.
        """
        # DP, start with coin
        dp_count = [0] + amount * [inf]
        
        for coin in coins:
            for sub_amount in range(coin, amount+1):
                if sub_amount - coin >= 0:
                    dp_count[sub_amount] = min(dp_count[sub_amount], dp_count[sub_amount - coin] + 1)
        
        return dp_count[amount] if dp_count[amount] < inf else -1