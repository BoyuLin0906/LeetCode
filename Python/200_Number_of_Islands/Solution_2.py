class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        island_count = 0
        row_len, col_len = len(grid[0]), len(grid)
            
        for y_idx in range(col_len):
            for x_idx in range(row_len):
                if grid[y_idx][x_idx] == "1":
                    island_count += 1
                    
                    stack = [(y_idx, x_idx)]
                    while stack:
                        col_idx, row_idx = stack.pop()
                        if 0 <= col_idx <= col_len-1 and 0 <= row_idx <= row_len-1 and grid[col_idx][row_idx] == "1":
                            grid[col_idx][row_idx] = "0"
                            stack += [(col_idx+1, row_idx), (col_idx, row_idx+1), (col_idx-1, row_idx), (col_idx, row_idx-1)]
                    
        return island_count