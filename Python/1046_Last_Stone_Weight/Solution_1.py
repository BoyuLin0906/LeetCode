class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]
        data = [-i for i in stones]
        heapq.heapify(data)
        
        while len(data) != 1:
            num1, num2 = heapq.heappop(data), heapq.heappop(data)
            heapq.heappush(data, num1-num2)
        
        return -data[0]