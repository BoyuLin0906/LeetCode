class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        Runtime 1327 ms / Beats 88.49%
        Memory 60 MB / Beats 35.51%
        """
        points.sort(key=lambda x: (x[1]))
        prev_end = -inf
        count = 0

        for point in points:
            start = point[0]
            end = point[1]
            if start > prev_end:
                prev_end = end
                count += 1
    
        return count