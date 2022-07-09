class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))
        remaining_number = len(intervals)
        end = intervals[0][1]
        
        for i in range(1, remaining_number):
            if intervals[i][1] <= end:
                remaining_number -= 1
            else:
                end = intervals[i][1]
                
        return remaining_number