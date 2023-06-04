class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Runtime 192 ms / Beats 68.53%
        Memory 16.5 MB / Beats 61.86%
        """
        # BFS
        num_len = len(isConnected[0])
        visited_point = set()

        def bfs(point):
            province = [point]
            while province:
                p = province.pop()
                for next_point, is_connected in enumerate(isConnected[p]):
                    if not next_point in visited_point and is_connected:
                        visited_point.add(next_point)
                        province.append(next_point)

        count = 0
        for i in range(num_len):
            if not i in visited_point:
                bfs(i)
                count += 1
    
        return count