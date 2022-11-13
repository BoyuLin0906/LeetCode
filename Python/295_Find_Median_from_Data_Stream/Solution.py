import heapq

class MedianFinder:
    """
    Runtime 593 ms / Beats 88.59%
    Memory 35.7 MB / Beats 80.14%
    """
    # two heap
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap, -num)
        to_max_value = -heapq.heappop(self.min_heap)
        heapq.heappush(self.max_heap, to_max_value)
        
        if len(self.max_heap) > len(self.min_heap):
            to_min_value = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, to_min_value)
        
    def findMedian(self) -> float:
        if len(self.max_heap) < len(self.min_heap):
            return float(-self.min_heap[0])
        else:
            return (self.max_heap[0]-self.min_heap[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()