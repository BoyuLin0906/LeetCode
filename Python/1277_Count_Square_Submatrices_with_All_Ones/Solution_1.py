"""
Runtime 87 ms, Beats 35.80% 
Memory 19.43 MB, Beats 15.81%
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row_len = len(matrix)
        col_len = len(matrix[0])

        total = 0
        dp = [[0 for _ in range(col_len+1)] for _ in range(row_len+1)]

        for row_idx in range(row_len):
            for col_idx in range(col_len):
                total += self.helper(row_idx, col_idx, matrix, dp)

        return total

    def helper(self, row_idx, col_idx, matrix, dp):
        row_len = len(matrix)
        col_len = len(matrix[0])

        if matrix[row_idx][col_idx] == 0:
            return 0
        
        left = dp[row_idx+1][col_idx]
        diagonal = dp[row_idx][col_idx]
        upper = dp[row_idx][col_idx+1]

        dp[row_idx+1][col_idx+1] = 1 + min(left, diagonal, upper)
        return dp[row_idx+1][col_idx+1]