"""
Runtime 577 ms / Beats 5.01%
Memory 36.46 MB / Beats 85.81%
"""

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        dsjoint_set = DisjointSet(n)
        for connection in connections:
            dsjoint_set.union(connection[0], connection[1])

        sets = len(dsjoint_set)
        return sets-1
        

class DisjointSet:
    def __init__(self, elements):
        self.parent = self.create_parent(elements)
        self.count = elements

    def create_parent(self, elements):
        return [element for element in range(elements)]

    def union(self, first_element, second_element):
        first_parent = self.find(first_element)
        second_parent = self.find(second_element)
        if first_parent != second_parent:
            self.parent[second_parent] = first_parent
            self.count -= 1
    
    def find(self, element):
        current_parent = self.parent[element]
        while self.parent[current_parent] != current_parent:
            current_parent = self.parent[current_parent]
        return current_parent

    def __len__(self):
        return self.count