class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Runtime: 6038 ms, faster than 5.00% of Python3 online submissions for Network Delay Time.
        Memory Usage: 17 MB, less than 13.69% of Python3 online submissions for Network Delay Time.
        """
        times_dict = defaultdict(list)
        result_list = [0] + [inf] * n
        
        for time in times: 
            times_dict[time[0]].append((time[1], time[2]))
        
        # DFS
        def DFS(node, node_weight):
            if result_list[node] > node_weight:
                result_list[node] = node_weight
                for target, weight in times_dict[node]:
                     DFS(target, node_weight + weight)
        
        DFS(k, 0)
        max_weight = max(result_list)
        
        return max_weight if max_weight < inf else -1