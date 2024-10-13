class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times_with_idx = list()
        for idx in range(len(times)):
            time = times[idx]
            arrival = time[0]
            leaving = time[1]
            times_with_idx.append((arrival, leaving, idx))

        times_with_idx.sort(key=lambda x: x[0])

        leaving_chairs = list() 
        available_chairs = list() 
        next_chair = 0
        for time in times_with_idx:
            arrival, leaving, idx = time
            while leaving_chairs and leaving_chairs[0][0] <= arrival:
                _, leaving_chair_idx = heapq.heappop(leaving_chairs)
                heapq.heappush(available_chairs, leaving_chair_idx)

            current_chair = next_chair
            if available_chairs:
                current_chair = heapq.heappop(available_chairs)
            else:
                next_chair += 1

            if idx == targetFriend:
                return current_chair

            heapq.heappush(leaving_chairs, (leaving, current_chair))

        return 0