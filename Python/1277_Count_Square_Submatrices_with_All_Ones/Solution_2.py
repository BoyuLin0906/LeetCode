"""
Runtime 63 ms, Beats 58.02% 
Memory 19.51 MB, Beats 14.49%
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row_len = len(matrix)
        col_len = len(matrix[0])

        total = 0
        dp = [[0 for _ in range(col_len+1)] for _ in range(row_len+1)]

        for row_idx in range(row_len):
            for col_idx in range(col_len):
                if matrix[row_idx][col_idx] == 0:
                    continue

                left = dp[row_idx+1][col_idx]
                diagonal = dp[row_idx][col_idx]
                upper = dp[row_idx][col_idx+1]

                dp[row_idx+1][col_idx+1] = 1 + min(left, diagonal, upper)
                total += dp[row_idx+1][col_idx+1]

        return total