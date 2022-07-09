class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]
        
        while len(stones) != 1:
            stones.sort()
            num1, num2 = stones.pop(), stones.pop()
            stones.append(num1-num2)
            
        return stones[0]