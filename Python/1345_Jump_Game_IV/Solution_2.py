class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """
        Runtime 788 ms / Beats 67.81%
        Memory 28.9 MB / Beats 60.49%
        """
        #  optimize solution 1 using set
        arr_len = len(arr)
        if arr_len == 1: return 0

        idx_dict = collections.defaultdict(list)
        for idx in range(arr_len):
            idx_dict[arr[idx]].append(idx)

        step = 0
        level_idxs = {0}
        visited = {0}
        while step < arr_len:
            temp_level_idxs = set()
            for idx in level_idxs:
                if idx == arr_len-1:
                    return step
                 
                temp_idx_list = idx_dict[arr[idx]] + [idx+1, idx-1]
                for next_idx in temp_idx_list:
                    if  0 < next_idx  < arr_len and not next_idx in visited:
                        temp_level_idxs.add(next_idx)
                        visited.add(next_idx)
                del idx_dict[arr[idx]]

            level_idxs = temp_level_idxs
            step += 1
        return arr_len-1