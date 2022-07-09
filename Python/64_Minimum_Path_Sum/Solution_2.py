class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Runtime: 165 ms, faster than 41.82% of Python3 online submissions for Minimum Path Sum.
        Memory Usage: 15.8 MB, less than 54.06% of Python3 online submissions for Minimum Path Sum.
        """
        # DP
        row_len = len(grid[0])
        col_len = len(grid)
        
        for row_idx in range(1, row_len):
            grid[0][row_idx] += grid[0][row_idx-1]
        for col_idx in range(1, col_len):
            grid[col_idx][0] += grid[col_idx-1][0]
        for col_idx in range(1, col_len):
            for row_idx in range(1, row_len):
                grid[col_idx][row_idx] += min(grid[col_idx-1][row_idx], grid[col_idx][row_idx-1])
        
        return grid[col_len-1][row_len-1]