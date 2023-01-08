class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """
        Runtime 862 ms / Beats 92.65%
        Memory 28 MB / Beats 62.34%
        """
        costs.sort()
        count = 0
        
        for cost in costs:
            if coins < cost:
                break
            else:
                coins -= cost
                count += 1
        
        return count