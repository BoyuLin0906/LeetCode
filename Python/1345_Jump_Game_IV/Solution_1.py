class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """
        Runtime 1471 ms / Beats 13.50%
        Memory 30.3 MB / Beats 24.88%
        """
        #  BFS
        idx_dict = collections.defaultdict(list)
        arr_len = len(arr)

        for idx in range(arr_len):
            idx_dict[arr[idx]].append(idx)

        step = 0
        queue = [0]
        visited = [True] + (arr_len-1) * [False]
        while step < arr_len:
            queue_len = len(queue)
            for _ in range(queue_len):
                idx = queue.pop(0)
                if idx == arr_len-1:
                    return step

                temp_idx_list = idx_dict[arr[idx]]
                temp_idx_list.append(idx+1)
                temp_idx_list.append(idx-1)
                for next_idx in temp_idx_list:
                    if  0 < next_idx  < arr_len and not visited[next_idx]:
                        queue.append(next_idx)
                        visited[next_idx] = True
                temp_idx_list.clear()
            step += 1
        return arr_len-1