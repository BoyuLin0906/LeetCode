class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        Runtime 657 ms, Beats 87.75%
        Memory 25.9 MB, Beats 89.18%
        """
        # sort + heap queue
        heap = []
        tmp_max_profit = 0
        data = list(zip(endTime, startTime, profit))
        data.sort(key=lambda x: x[1])

        for idx in range(0, len(profit)):
            end_time_idx, start_time_idx, tmp_profit = data[idx][0], data[idx][1], data[idx][2]
            while heap and start_time_idx >= heap[0][0]:
                heap_data = heappop(heap)
                tmp_max_profit = max(heap_data[1], tmp_max_profit)
            heappush(heap, (end_time_idx, tmp_profit + tmp_max_profit))

        res = 0
        while heap:
            heap_data = heappop(heap)
            res = max(res, heap_data[1])

        return res