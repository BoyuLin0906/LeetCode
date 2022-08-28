class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
		Runtime: 39 ms, faster than 89.47% of Python3 online submissions for Rotate Image.
		Memory Usage: 14 MB, less than 30.10% of Python3 online submissions for Rotate Image.
        """
        """
		1  2  3　　　 　　 9  6  3　　　　　     7  4  1

		4  5  6　　-->　　 8  5  2　　 -->   　  8  5  2　　

		7  8  9 　　　 　　7  4  1　　　　　     9  6  3
        """
        matrix_len = len(matrix)
        for i in range(matrix_len-1):
            for j in range(matrix_len-i-1):
                matrix[i][j], matrix[matrix_len-1-j][matrix_len-1-i] = matrix[matrix_len-1-j][matrix_len-1-i], matrix[i][j]
        matrix.reverse()