class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """
        Runtime: 2835 ms, faster than 24.03% of Python3 online submissions for Range Sum Query 2D - Immutable.
        Memory Usage: 25.7 MB, less than 18.36% of Python3 online submissions for Range Sum Query 2D - Immutable.
        """
        # Prefix Sum
        row_len = len(matrix)
        col_len = len(matrix[0])
        self.matrix = [[0 for _ in range(col_len+1)] for _ in range(row_len+1)]
        
        for row_idx in range(row_len):
            for col_idx in range(col_len):
                print(row_idx, col_idx)
                self.matrix[row_idx+1][col_idx+1] = self.matrix[row_idx+1][col_idx] + matrix[row_idx][col_idx] 
                
        for col_idx in range(col_len):
            for row_idx in range(row_len):
                self.matrix[row_idx+1][col_idx+1] = self.matrix[row_idx+1][col_idx+1] + self.matrix[row_idx][col_idx+1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2+1][col2+1] - self.matrix[row1][col2+1] - self.matrix[row2+1][col1] + self.matrix[row1][col1]
        
    

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)