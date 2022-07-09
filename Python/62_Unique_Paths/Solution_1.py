class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    	# DP
        dp_table = [[1] * n for i in range(m)]
        
        for row in range(1, m):
            for column in range(1, n):
                dp_table[row][column] = dp_table[row-1][column] + dp_table[row][column-1]
        
        return dp_table[m-1][n-1]