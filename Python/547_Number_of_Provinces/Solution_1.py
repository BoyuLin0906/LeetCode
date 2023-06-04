class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Runtime 200 ms / Beats 45.44%
        Memory 16.8 MB / Beats 40.79%
        """
        # union find
        num_len = len(isConnected[0])
        num_set = DisjointSet([i for i in range(num_len)])
        
        # union
        for i in range(num_len):
            for j in range(num_len):
                if isConnected[i][j]:
                    num_set.union(i, j)

        # count sets
        result_set = set()
        for i in range(num_len):
            result_set.add(num_set.find(i))

        return len(result_set)


class DisjointSet:
    def __init__(self, elements):
        self.parents = {element:element for element in elements}

    def find(self, element):
        if element in self.parents:
            n = self.parents[element]
            while self.parents[n] != n:
                n = self.parents[n]
            return n
        return element
            
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            if u > v:
                self.parents[u] = v
            else:
                self.parents[v] = u