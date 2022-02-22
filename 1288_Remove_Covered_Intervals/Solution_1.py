class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1]-interval[0])
        intervals_length = len(intervals)
        results = []
        
        for i in range(intervals_length):
            results.append(intervals[i])
            for j in range(intervals_length-1, i, -1):
                if intervals[j][0] <= intervals[i][0] and intervals[j][1] >= intervals[i][1]:
                    results.pop()
                    break
                    
        return len(results)