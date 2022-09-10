class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res_intervals = list()    
        intervals.sort(key = lambda x: x[0])
        
        """
        Runtime: 158 ms, faster than 89.57% of Python3 online submissions for Merge Intervals.
        Memory Usage: 18.1 MB, less than 85.10% of Python3 online submissions for Merge Intervals.
        """
        for idx in range(len(intervals)):
            interval = intervals[idx]
            
            if res_intervals and res_intervals[-1][1] >= interval[0]:
                res_intervals[-1][1] = max(res_intervals[-1][1], interval[1])
            else:
                res_intervals.append(interval)
            
        return res_intervals