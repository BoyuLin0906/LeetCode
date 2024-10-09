class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num_to_rank = dict() 
        sorted_arr = sorted(arr)
        arr_len = len(arr)
        
        rank = 1
        for idx in range(arr_len):
            if idx > 0 and sorted_arr[idx] != sorted_arr[idx-1]:
                rank += 1
            num_to_rank[sorted_arr[idx]] = rank

        for idx in range(arr_len):
            arr[idx] = num_to_rank[arr[idx]]

        return arr