class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        Runtime: 1298 ms, faster than 25.72% of Python3 online submissions for Cherry Pickup.
        Memory Usage: 14.1 MB, less than 97.40% of Python3 online submissions for Cherry Pickup.
        """
        # db + for loop
        n = len(grid)
        # weight + height -1 
        total_step = n * 2 - 1
        dp_table = [[float('-inf')] * n for _ in range(n)]
        dp_table[0][0] = grid[0][0]
        
        for step in range(1, total_step):
            dp2_table = [[float('-inf')] * n for _ in range(n)]
            # person_1
            for i_1 in range(n):
                # person_2
                for i_2 in range(n):
                    j_1 = step - i_1
                    j_2 = step - i_2
                    if (j_1 < 0 or j_1 >= n or j_2 < 0 or j_2 >= n or 
                        grid[i_1][j_1] == -1 or grid[i_2][j_2] == -1):
                        continue
                    
                    res = grid[i_1][j_1]
                    if j_1 != j_2 and i_1 != i_2: res += grid[i_2][j_2]
                    
                    # (i_1, j_1-1, i_2, j_2-1)
                    temp = dp_table[i_1][i_2]
                    # (i_1-1, j_1, i_2, j_2-1)
                    if i_1 > 0: temp = max(temp, dp_table[i_1-1][i_2])
                    # (i_1, j_1-1, i_2-1, j_2)
                    if i_2 > 0: temp = max(temp, dp_table[i_1][i_2-1])
                    # (i_1-1, j_1, i_2-1, j_2)
                    if i_1 > 0 and i_2 > 0: temp = max(temp, dp_table[i_1-1][i_2-1])
                    if temp >= 0: dp2_table[i_1][i_2] = res + temp
            dp_table = dp2_table
            
        return max(0, dp_table[n-1][n-1])