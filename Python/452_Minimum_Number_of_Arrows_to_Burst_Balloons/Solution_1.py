class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        Runtime 1370 ms / Beats 80.44%
        Memory 60 MB / Beats 35.51%
        """
        points.sort(key=lambda x: (x[0], x[1]))
        prev_end = -inf
        count = 0
        
        for point in points:
            start = point[0]
            end = point[1]
            # overlapping
            if start <= prev_end:
                prev_end = min(prev_end, end)
            else: 
                prev_end = end
                count += 1

        return count