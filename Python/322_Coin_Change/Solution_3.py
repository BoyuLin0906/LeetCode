class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Runtime: 831 ms, faster than 96.01% of Python3 online submissions for Coin Change.
        Memory Usage: 14.2 MB, less than 61.96% of Python3 online submissions for Coin Change.
        """
        # DP + BFS
        if amount == 0: return 0
        
        dp_count = [0] * (amount + 1)
        queue = deque([(amount, 0)])
        
        while queue:
            remained_amount, count = queue.popleft()
            
            for coin in coins:
                tmp_amount = remained_amount - coin
                
                if tmp_amount > 0 and dp_count[tmp_amount] == 0:
                    dp_count[tmp_amount] = count + 1
                    queue.append([tmp_amount, count + 1])
                elif tmp_amount == 0:
                    return count + 1
        return -1