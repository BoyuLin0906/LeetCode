class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
		Runtime: 1284 ms, faster than 78.96% of Python3 online submissions for Min Cost to Connect All Points.
		Memory Usage: 14.5 MB, less than 88.74% of Python3 online submissions for Min Cost to Connect All Points.
        """
        # Prim’s MST
        points_dict = {(points[idx][0], points[idx][1]): inf if idx else 0 for idx in range(len(points))}
        dist = 0
        
        while points_dict:
            x, y = min(points_dict, key=points_dict.get)
            dist += points_dict.pop((x, y))
            
            for (x1, y1) in points_dict.keys():
                points_dict[(x1, y1)] = min(points_dict[(x1, y1)], abs(x1-x)+abs(y1-y))
                
        return dist