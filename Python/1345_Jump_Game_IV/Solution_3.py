class Solution:
    def minJumps(self, arr: List[int]) -> int:
        """
        Runtime 622 ms / Beats 98.86%
        Memory 28.6 MB / Beats 78.70%
        """
        # bi-directional BFS using set
        arr_len = len(arr)
        if arr_len == 1: return 0

        idx_dict = collections.defaultdict(list)
        for idx in range(arr_len):
            idx_dict[arr[idx]].append(idx)

        step = 0
        visited = {0, arr_len-1}
        seq_1 = {0}
        seq_2 = {arr_len-1} 
        while seq_1:
            if len(seq_1) > len(seq_2):
                seq_1, seq_2 = seq_2, seq_1

            temp_seq = set()
            while seq_1:
                idx = seq_1.pop()
                temp_idx_list = idx_dict[arr[idx]] + [idx+1, idx-1]
                for next_idx in temp_idx_list:
                    if next_idx in seq_2:
                        return step+1
                    if next_idx in visited:
                        continue
                    if 0 <= next_idx < arr_len:
                        temp_seq.add(next_idx)
                        visited.add(next_idx)
                del idx_dict[arr[idx]]

            seq_1 = temp_seq
            step += 1
        return arr_len-1