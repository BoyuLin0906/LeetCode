class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        Runtime 1742 ms / Beats 99.90%
        Memory 63.1 MB / Beats 32.68%
        """
        for idx, task in enumerate(tasks):
            task.append(idx)  
        # sort by enqueue time
        tasks.sort(key=lambda task:task[0])
        
        queue = []
        res = []
        time = 0
        for task in tasks:
            enqueue_time = task[0]
            processing_time = task[1]
            index = task[2]

            while queue and enqueue_time > time:
                process_t, idx = heapq.heappop(queue)
                res.append(idx)
                time += process_t

            time = max(time, enqueue_time)
            heapq.heappush(queue, (processing_time, index))

        # sort by processing time
        queue.sort()
        return res + [idx for _, idx in queue]