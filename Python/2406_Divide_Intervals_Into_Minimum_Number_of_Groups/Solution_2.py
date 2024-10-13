"""
Runtime 3385 ms / Beats 5.16%
Memory 61.51 MB / Beats 10.91%
"""

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        interval_start = 10**6 + 1
        interval_end = -1
        for interval in intervals:
            left = interval[0]
            interval_start = min(interval_start, left)
            right = interval[1]
            interval_end = max(interval_end, right)

        point_to_count = [0] * (interval_end+2)
        for interval in intervals:
            left = interval[0]
            point_to_count[left] += 1
            right = interval[1]
            point_to_count[right+1] -= 1

        current_group = 0
        max_group = 0
        for idx in range(interval_start, interval_end+1):
            current_group += point_to_count[idx]
            max_group = max(max_group, current_group)
            
        return max_group
