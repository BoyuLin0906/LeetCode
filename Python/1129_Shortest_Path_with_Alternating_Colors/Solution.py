class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        """
        Runtime 95 ms / Beats 49.71%
        Memory 14.2 MB / Beats 31.23%
        """
        # BFS + Graph

        red_edge_dict = collections.defaultdict(list)
        red_edge_visited = dict()
        blue_edge_dict = collections.defaultdict(list)
        blue_edge_visited = dict()

        # build the graph and its visited table
        for edge in redEdges:
            red_edge_dict[edge[0]].append(edge[1])
            red_edge_visited[(edge[0], edge[1])] = False
        
        for edge in blueEdges:
            blue_edge_dict[edge[0]].append(edge[1])
            blue_edge_visited[(edge[0], edge[1])] = False

        # initialize the queue from `0 node` to `next node`
        queue = []
        for next_node in red_edge_dict[0]:
            queue.append(("red", next_node, 1))

        for next_node in blue_edge_dict[0]:
            queue.append(("blue", next_node, 1))

        # run the alternating color edges (BFS)
        res = [inf] * n
        while queue:
            color, node, length = queue.pop(0)
            res[node] = min(res[node], length)
            # red -> blue
            if color == "red":
                for next_node in blue_edge_dict[node]:
                    if not blue_edge_visited[(node, next_node)]:
                        blue_edge_visited[(node, next_node)] = True
                        queue.append(("blue", next_node, length+1))
            # blue -> red
            elif color == "blue":
                for next_node in red_edge_dict[node]:
                    if not red_edge_visited[(node, next_node)]:
                        red_edge_visited[(node, next_node)] = True
                        queue.append(("red", next_node, length+1)) 

        # change the `inf` value to -1
        res[0] = 0
        for idx in range(1,n):
            if res[idx] == inf:
                res[idx] = -1

        return res