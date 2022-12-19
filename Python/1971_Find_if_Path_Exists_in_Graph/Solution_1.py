class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        Runtime 1805 ms / Beats 95.83%
        Memory 116.3 MB / Beats 38.48%
        """
        # dict + queue + BFS
        graph = defaultdict(set)
        queue = []
        visited = set() 

        for node_1, node_2 in edges:
            graph[node_1].add(node_2)
            graph[node_2].add(node_1)

        queue.append(source)
        visited.add(source)

        while queue:
            node = queue.pop(0)
            if node == destination: return True

            for sub_node in graph[node]:
                if not sub_node in visited:
                    visited.add(sub_node)
                    queue.append(sub_node)
        
        return False