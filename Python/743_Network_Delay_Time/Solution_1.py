class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Runtime: 714 ms, faster than 30.01% of Python3 online submissions for Network Delay Time.
        Memory Usage: 16.6 MB, less than 48.51% of Python3 online submissions for Network Delay Time.
        """
        times_dict = defaultdict(dict)
        results = [0 for _ in range(n+1)]
        queue = [(0, k)]
        
        for time in times: 
            times_dict[time[0]][time[1]] = time[2]
        
        # Dijkstra's Algorithm
        while queue:
            source_weight, source = heapq.heappop(queue)
            if source in times_dict :
                for target, weight in times_dict[source].items():
                    new_weight = source_weight + weight
                    if (results[target] == 0 or results[target] > new_weight) and target != k:
                        results[target] = new_weight
                        heapq.heappush(queue, (new_weight, target))

        return  max(results) if results.count(0) <= 2 else -1