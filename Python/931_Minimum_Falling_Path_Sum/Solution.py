class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        Runtime 167 ms / Beats 83.45% 
        Memory 14.8 MB / Beats 40.57%
        """
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        for row_idx in range(1, row_len):
            for col_idx in range(col_len):
                same_col = matrix[row_idx-1][col_idx]
                left_col = inf
                right_col = inf

                if col_idx-1 != -1:
                    left_col = matrix[row_idx-1][col_idx-1]

                if col_idx+1 != col_len:
                    right_col = matrix[row_idx-1][col_idx+1]

                matrix[row_idx][col_idx] += min(same_col, left_col, right_col)

        return min(matrix[-1])