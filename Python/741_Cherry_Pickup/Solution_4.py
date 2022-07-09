class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        Runtime: 816 ms, faster than 70.91% of Python3 online submissions for Cherry Pickup.
        Memory Usage: 14.1 MB, less than 97.40% of Python3 online submissions for Cherry Pickup.
        """
        # db + for loop + optimization
        n = len(grid)
        total_step = n * 2 - 1
        dp_table = [[float('-inf')] * n for _ in range(n)]
        dp_table[0][0] = grid[0][0]
        
        for step in range(1, total_step):
            dp2_table = [[float('-inf')] * n for _ in range(n)]
            
            for i_1 in range(max(0, step-(n-1)), min(n-1, step) + 1):
                for i_2 in range(max(0, step-(n-1)), min(n-1, step) + 1):
                    j_1 = step - i_1
                    j_2 = step - i_2
                    if (grid[i_1][j_1] == -1 or grid[i_2][j_2] == -1):
                        continue
                        
                    temp = dp_table[i_1][i_2]
                    if i_1 > 0: temp = max(temp, dp_table[i_1-1][i_2])
                    if i_2 > 0: temp = max(temp, dp_table[i_1][i_2-1])
                    if i_1 > 0 and i_2 > 0: temp = max(temp, dp_table[i_1-1][i_2-1])
                    
                    res = grid[i_1][j_1]
                    if j_1 != j_2 and i_1 != i_2: res += grid[i_2][j_2]
                    dp2_table[i_1][i_2] = res + temp
                    
            dp_table = dp2_table
            
        return max(0, dp_table[n-1][n-1])