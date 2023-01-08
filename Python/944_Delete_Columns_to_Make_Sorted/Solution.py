class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        Runtime 148 ms / Beats 90.78%
        Memory 14.6 MB / Beats 92.10%
        """
        strs_list_len = len(strs)
        str_len = len(strs[0])
        if strs_list_len == 1: return 0 
        
        count = 0
        for idx in range(str_len):
            for list_idx in range(1, strs_list_len):
                if strs[list_idx-1][idx] > strs[list_idx][idx]:
                    count += 1
                    break

        return count