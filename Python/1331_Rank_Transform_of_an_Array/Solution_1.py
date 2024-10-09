"""
Runtime 286 ms / Beats 10.90%
Memory 46.51 MB / Beats 5.00%
"""

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks_mapping = dict()
        
        for idx in range(len(arr)):
            ranks_mapping[idx] = arr[idx]

        ranks_mapping = dict(sorted(ranks_mapping.items(), key=lambda mapping: mapping[1]))
        
        prev_value = (10**9) + 1
        rank = 0
        for idx, value in ranks_mapping.items():
            if prev_value != value:
                rank += 1
            arr[idx] = rank
            prev_value = value

        return arr