class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # button up dp
        n = len(grid)
        # person_1 (col_1, row_1)
        # person_2 (col_2, row_2)
        
        dp_table = [[[None] * n for _ in range(n)] for _ in range(n)]
        
        def dp(row_1, col_1, row_2):
            # both have one step
            col_2 = row_1 + col_1 - row_2
            
            # border or -1
            if (row_1 == -1 or col_1 == -1 or row_2 == -1 or col_2 == -1 or
                grid[row_1][col_1] == -1 or grid[row_2][col_2] == -1):
                return float("-inf")
            # origin
            elif row_1 == 0 and col_1 == 0:
                return grid[0][0]
            # dp has value
            elif dp_table[row_1][col_1][row_2] is not None:
                return dp_table[row_1][col_1][row_2]
            else:
                res = grid[row_1][col_1]
                # same position
                if col_2 != col_1 and row_2 != row_1: res +=  grid[row_2][col_2]
                
                res += max(dp(row_1-1, col_1, row_2-1), dp(row_1, col_1-1, row_2),
                           dp(row_1, col_1-1, row_2-1), dp(row_1-1, col_1, row_2))
                # save max in dp
                dp_table[row_1][col_1][row_2] = res
                return res
            
        return max(0, dp(n-1, n-1, n-1))