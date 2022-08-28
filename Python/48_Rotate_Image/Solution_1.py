class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Runtime: 34 ms, faster than 96.55% of Python3 online submissions for Rotate Image.
        Memory Usage: 13.9 MB, less than 30.10% of Python3 online submissions for Rotate Image.
        """
        """
        1  2  3               7  2  1            7  4  1

        4  5  6      -->      4  5  6　　 -->  　 8  5  2　　

        7  8  9               9  8  3　　　　   　9  6  3
        """
        matrix_len = len(matrix)
        for i in range(int(matrix_len/2)):
            for j in range(i, matrix_len-i-1):
                temp = matrix[i][j] 
                matrix[i][j] = matrix[matrix_len-j-1][i]
                matrix[matrix_len-j-1][i] = matrix[matrix_len-i-1][matrix_len-j-1]
                matrix[matrix_len-i-1][matrix_len-j-1] = matrix[j][matrix_len-i-1]
                matrix[j][matrix_len-i-1] = temp