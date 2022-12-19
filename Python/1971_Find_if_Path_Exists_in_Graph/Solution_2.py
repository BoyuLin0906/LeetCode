class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        Runtime 2043 ms / Beats 86.12% 
        Memory 103.5 MB / Beats 91.76%
        """
        # UnionFind
        graph = UnionFind(n)
        for node_1, node_2 in edges:
            graph.union(node_1, node_2)
        
        node_1 = graph.find(source)
        node_2 = graph.find(destination)
        
        return node_1 == node_2

class UnionFind:
    def __init__(self, elements):
        self.parents = [n for n in range(elements)]
        
    def find(self, node):
        node = self.parents[node]
        while self.parents[node] != node:
            node = self.parents[node]
        return node
        
    def union(self, node_1, node_2):
        node_1 = self.find(node_1)
        node_2 = self.find(node_2)
        if node_1 != node_2:
            self.parents[node_1] = node_2