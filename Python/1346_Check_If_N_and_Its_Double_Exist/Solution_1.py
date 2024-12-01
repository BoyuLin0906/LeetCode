"""
Runtime 3 ms / Beats 57.43%
Memory 17.56 MB / Beats 5.25%
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()

        check_table = dict()
        for idx in range(len(arr)):
            check_table[arr[idx]] = idx

        for idx in range(len(arr)):
            prod = arr[idx] * 2
            if prod in check_table and check_table[prod] != idx:
                return True

        return False