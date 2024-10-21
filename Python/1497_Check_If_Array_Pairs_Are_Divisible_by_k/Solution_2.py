"""
Runtime 473 ms / Beats 79.70%
Memory 30.38 MB / Beats 66.50%
"""

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        num_counter = [0] * k
        for num in arr:
            num = ((num % k) + k) % k
            num_counter[num] += 1
        
        if num_counter[0] % 2 != 0:
            return False

        for idx in range(1, (k//2)+1):
            if num_counter[idx] != num_counter[k - idx]:
                return False

        return True