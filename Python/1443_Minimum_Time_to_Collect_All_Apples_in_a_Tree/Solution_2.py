class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """
        Runtime 645 ms / Beats 90.44%
        Memory 51.5 MB / Beats 41.5%
        """
        if not any(hasApple): return 0
        
        tree_map = defaultdict(list)
        for edge in edges:
            n1 = edge[0]
            n2 = edge[1]
            tree_map[n2].append(n1)
            tree_map[n1].append(n2)

        def dfs(node, parent_node):
            res_path = 0
            if node in tree_map:
                for child_node in tree_map[node]:
                    if child_node != parent_node:
                        res_path += dfs(child_node, node)

            if hasApple[node] or res_path:
                return res_path + 2

            return 0
        
        res = dfs(0, -1)
        return res-2
