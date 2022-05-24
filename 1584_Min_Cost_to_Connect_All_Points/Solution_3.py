class uf_ds:
    def __init__(self, parent):
        self.parent_node = parent

    def find(self, k):
        if self.parent_node[k] == k: return k
        return self.find(self.parent_node[k])

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        self.parent_node[x] = y
    
    def is_cycle(self, a, b):
        return self.find(a) == self.find(b)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Runtime: 1933 ms, faster than 55.42% of Python3 online submissions for Min Cost to Connect All Points.
        Memory Usage: 103.7 MB, less than 30.11% of Python3 online submissions for Min Cost to Connect All Points.
        """
        # Kruskal’s Minimum Spanning Tree Algorithm
        points_len = len(points)
        egdes, union = list(), list()
        dist, count = 0, 0
        
        # find all paths
        for idx_1 in range(points_len):
            union.append(idx_1)
            for idx_2 in range(idx_1+1, points_len):
                egdes.append([idx_1, idx_2, 
                              abs(points[idx_1][0] - points[idx_2][0]) +  abs(points[idx_1][1] - points[idx_2][1])])
        
        # sort all paths by its distance
        egdes.sort(key=lambda x: x[2])
        count = 0
        
        # make set
        data = uf_ds(union)
        
        # connet all egde and union the points
        for edge in egdes:
            if points_len-1 == count: break
            if not data.is_cycle(edge[0], edge[1]):
                dist += edge[2]
                data.union(edge[0], edge[1])
                count += 1
            
        return dist