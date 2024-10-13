"""
Runtime 1129 ms / Beats 50.00%
Memory 56.34 MB / Beats 50.20%
"""

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        groups = list()
        intervals.sort(key=lambda x: (x[0], x[1]))

        for interval in intervals:
            left = interval[0]
            right = interval[1]
            
            if groups and groups[0] < left:
                heapq.heappop(groups)
                
            heapq.heappush(groups, right)
        
        return len(groups)