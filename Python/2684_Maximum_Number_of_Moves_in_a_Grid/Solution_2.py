"""
Runtime 331 ms / Beats 21.21%
Memory 27.26 MB / Beats 84.81%
"""

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        
        dp = [[0 for _ in range(col_len)] for _ in range(row_len)]
        for row_idx in range(row_len):
            dp[row_idx][0] = 1

        max_moves = 0
        for col_idx in range(1, col_len):
            for row_idx in range(row_len):
                if row_idx+1 < row_len and grid[row_idx][col_idx] > grid[row_idx+1][col_idx-1] and dp[row_idx+1][col_idx-1] > 0:
                    dp[row_idx][col_idx] = max(dp[row_idx][col_idx], dp[row_idx+1][col_idx-1] + 1)
                
                if grid[row_idx][col_idx] > grid[row_idx][col_idx-1] and dp[row_idx][col_idx-1] > 0:
                    dp[row_idx][col_idx] = max(dp[row_idx][col_idx], dp[row_idx][col_idx-1] + 1)

                if row_idx-1 >= 0 and grid[row_idx][col_idx] > grid[row_idx-1][col_idx-1] and dp[row_idx-1][col_idx-1] > 0:
                    dp[row_idx][col_idx] = max(dp[row_idx][col_idx], dp[row_idx-1][col_idx-1] + 1)

                max_moves = max(max_moves, dp[row_idx][col_idx]-1)

        return max_moves