"""
Runtime 0 ms / Beats 100%
Memory 17.47 MB / Beats 5.25%
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        visited = set()
        for num in arr:
            double_val = 2 * num
            divide_val = num // 2
            if double_val in visited or (num % 2 == 0 and divide_val in visited):
                return True
            visited.add(num)

        return False