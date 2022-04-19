class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        island_count = 0
        row_len, column_len = len(grid[0]), len(grid)
        
        def recover_area(column_idx, row_idx):
            if 0 > column_idx or column_idx > column_len-1 or 0 > row_idx or row_idx > row_len-1: return
            if grid[column_idx][row_idx] == "0": return
        
            grid[column_idx][row_idx] = "0"
            # up
            recover_area(column_idx-1, row_idx)
            # down
            recover_area(column_idx+1, row_idx)
            # left
            recover_area(column_idx, row_idx-1)
            # right
            recover_area(column_idx, row_idx+1)
            
        for y_idx in range(column_len):
            for x_idx in range(row_len):
                if grid[y_idx][x_idx] == "1":
                    island_count += 1
                    recover_area(y_idx, x_idx)
                    
        return island_count