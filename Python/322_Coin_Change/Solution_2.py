class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    	"""
		Runtime: 1836 ms, faster than 57.04% of Python3 online submissions for Coin Change.
		Memory Usage: 14.1 MB, less than 61.96% of Python3 online submissions for Coin Change.
    	"""
        # DP, start with amount
        dp_count = [0] + amount * [inf]
        
        for sub_amount in range(amount+1):
            for coin in coins:
                if sub_amount - coin >= 0:
                    dp_count[sub_amount] = min(dp_count[sub_amount], dp_count[sub_amount - coin] + 1)
        
        return dp_count[amount] if dp_count[amount] < inf else -1