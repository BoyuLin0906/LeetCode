class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        Runtime 32 ms / Beats 72.90%
        Memory 13.9 MB / Beats 69.83%
        """
        col_idx = row_idx = 0
        direction = [0, 1]
        matrix  = [[0 for j in range(n)] for i in range(n)]
       
        for value in range(n*n):
            matrix[row_idx][col_idx] = value + 1
            if matrix[(row_idx+direction[0])%n][(col_idx+direction[1])%n]:
                direction[0], direction[1] = direction[1], -direction[0]
            row_idx += direction[0]
            col_idx += direction[1]

        return matrix