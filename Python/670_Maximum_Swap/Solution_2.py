"""
Runtime 0 ms / Beats 100.00%
Memory 16.57 MB / Beats 61.15%
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)
        num_str = [ char for char in num_str ]
        num_len = len(num_str)
        last_seen = [-1] * 10

        for idx in range(num_len):
            last_seen[int(num_str[idx])] = idx

        for idx in range(num_len):
            for digit in range(9, int(num_str[idx]), -1):
                if last_seen[digit] > idx:
                    swap_idx = last_seen[digit]
                    num_str[swap_idx], num_str[idx] = num_str[idx], num_str[swap_idx]
                    return int("".join(num_str))
            
        return num