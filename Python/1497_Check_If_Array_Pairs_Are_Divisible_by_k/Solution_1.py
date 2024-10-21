"""
Runtime 4839 ms / Beats 5.11%
Memory 30.32 MB / Beats 66.50%
"""
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        process_arr = list()
        for num in arr:
            num = ((num % k) + k) % k
            process_arr.append(num)

        process_arr.sort()
        
        while len(process_arr) > 2:
            if process_arr[0] == 0 and process_arr[1] == 0:
                process_arr = process_arr[2:]
            else:
                break

        
        left_idx = 0
        right_idx = len(process_arr)-1
        while left_idx < right_idx:
            if (process_arr[left_idx] + process_arr[right_idx]) % k != 0:
                return False
            left_idx += 1
            right_idx -= 1

        return True