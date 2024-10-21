"""
Runtime 0 ms / Beats 100.00%
Memory 16.68 MB / Beats 26.54%
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = str(num)
        num = [ char for char in num ]
        num_len = len(num)

        for f_idx in range(num_len):

            max_val = '-1'
            idx = -1
            for s_idx in range(num_len-1, f_idx, -1):
                if num[s_idx] > num[f_idx] and num[s_idx] > max_val:
                    max_val = num[s_idx]
                    idx = s_idx
            
            if idx != -1:
                num[f_idx], num[idx] = num[idx], num[f_idx]
                break
        
        return int("".join(num))