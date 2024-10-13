"""
Runtime 363 ms / Beats 98.70%
Memory 36.80 MB / Beats 59.84%
"""

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        adjacent_graph = [[] for _ in range(n)] 
        for connection in connections:
            adjacent_graph[connection[0]].append(connection[1])
            adjacent_graph[connection[1]].append(connection[0])

        visited = [False] * n
        diff_networks = 0
        for idx in range(n):
            if not visited[idx]:
                dfs(idx, adjacent_graph, visited)
                diff_networks += 1
    
        return diff_networks - 1
        

def dfs(node, adjacent_graph, visited):
    visited[node] = True
    for next_node in adjacent_graph[node]:
        if not visited[next_node]:
            dfs(next_node, adjacent_graph, visited) 

