class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        """
		Runtime 1820 ms / Beats 92.80%
		Memory 29 MB / Beats 18.87%
        """
        for idx in range(len(piles)):
            piles[idx] = -piles[idx]
        heapq.heapify(piles)

        for idx in range(k):
            pile = heapq.heappop(piles)
            heapq.heappush(piles, pile//2)

        return -sum(piles)