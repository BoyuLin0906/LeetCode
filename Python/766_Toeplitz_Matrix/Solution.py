class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    	"""
		Runtime: 87 ms, faster than 95.97% of Python3 online submissions for Toeplitz Matrix.
		Memory Usage: 13.8 MB, less than 78.65% of Python3 online submissions for Toeplitz Matrix.
    	"""
        row_len, col_len = len(matrix), len(matrix[0])
        
        for row_idx in range(row_len-1):
            for col_idx in range(col_len-1):
                if matrix[row_idx][col_idx] != matrix[row_idx+1][col_idx+1]:
                    return False
        return True