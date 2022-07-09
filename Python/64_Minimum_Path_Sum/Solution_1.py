class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Runtime: 122 ms, faster than 75.63% of Python3 online submissions for Minimum Path Sum.
        Memory Usage: 15.8 MB, less than 54.06% of Python3 online submissions for Minimum Path Sum.
        """
        # DP
        row_len = len(grid[0])
        col_len = len(grid)
        
        for col_idx in range(col_len):
            for row_idx in range(row_len):
                _min = float(inf)
                if row_idx > 0: _min = min(_min, grid[col_idx][row_idx-1])
                if col_idx > 0: _min = min(_min, grid[col_idx-1][row_idx])
                grid[col_idx][row_idx] += _min if _min != float(inf) else 0
        
        return grid[col_len-1][row_len-1]