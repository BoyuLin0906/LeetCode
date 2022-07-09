class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Runtime: 500 ms, faster than 78.35% of Python3 online submissions for Network Delay Time.
        Memory Usage: 16.9 MB, less than 13.69% of Python3 online submissions for Network Delay Time.
        """
        times_dict = defaultdict(dict)
        nodes = set([k])
        queue = [(0, k)]
        
        for time in times: 
            times_dict[time[0]][time[1]] = time[2]
        
        # Dijkstra's Algorithm
        while queue:
            source_weight, source = heapq.heappop(queue)
            nodes.add(source)
            if len(nodes) == n: return source_weight
            
            if source in times_dict :
                for target, weight in times_dict[source].items():
                    if not target in nodes:
                        heapq.heappush(queue, (source_weight + weight, target))
                        
        return -1