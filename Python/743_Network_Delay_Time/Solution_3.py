class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Runtime: 661 ms, faster than 38.43% of Python3 online submissions for Network Delay Time.
        Memory Usage: 16.3 MB, less than 58.79% of Python3 online submissions for Network Delay Time.
        """
        times_dict = defaultdict(list)
        result_list = [0] + [inf] * n
        queue = deque([(0, k)])
        
        for time in times: 
            times_dict[time[0]].append((time[1], time[2]))
        
        # BFS
        while queue:
            node_weight, node = queue.popleft()
            if node_weight < result_list[node]:
                result_list[node] = node_weight
                for target, weight in times_dict[node]:
                    queue.append((node_weight + weight, target))
        max_weight = max(result_list)
        
        return max_weight if max_weight < inf else -1