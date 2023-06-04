class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Runtime 189 ms / Beats 77.56%
        Memory 17.3 MB / Beats 11.65%
        """
        # DFS
        num_len = len(isConnected[0])
        visited_point = set()

        def dfs(point):
            for next_point, is_connected in enumerate(isConnected[point]):
                if not next_point in visited_point and is_connected:
                    visited_point.add(next_point)
                    dfs(next_point)

        count = 0
        for i in range(num_len):
            if not i in visited_point:
                dfs(i)
                count += 1
    
        return count
    