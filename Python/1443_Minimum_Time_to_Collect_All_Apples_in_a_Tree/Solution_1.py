class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """
        Runtime 679 ms / Beats 71.5%
        Memory 51.9 MB / Beats 39.79%
        """
        if not any(hasApple): return 0
        
        tree_map = defaultdict(list)
        visited = [False] * n

        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]
            tree_map[n2].append(n1)
            tree_map[n1].append(n2)

        def dfs(node, step):
            visited[node] = True
            child_path = 0
            if node in tree_map:
                for child_node in tree_map[node]:
                    if not visited[child_node]:
                        child_res = dfs(child_node, step+1)
                        if child_path != 0 and child_res:
                            child_path -= step
                        child_path += child_res

            if child_path:
                return child_path
            elif hasApple[node]:
                return step
            return 0
        
        res = dfs(0, 0)

        return res*2
