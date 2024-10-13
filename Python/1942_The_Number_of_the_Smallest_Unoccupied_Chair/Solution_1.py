class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        times_len = len(times)

        friends_arrival_idxes = dict()
        for idx in range(times_len):
            friends_arrival_idxes[times[idx][0]] = idx

        chairs = [[]] * times_len
        times.sort(key=lambda x: x[0])
        
        for time in times:
            occupied_key = time
            for idx in range(times_len):
                if chairs[idx] and chairs[idx][1] > occupied_key[0]:
                    continue
                
                if friends_arrival_idxes[occupied_key[0]] == targetFriend:
                    return idx

                chairs[idx] = occupied_key
                break

        return 0