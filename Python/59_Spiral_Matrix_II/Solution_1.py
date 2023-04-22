class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        Runtime 33 ms / Beats 62.69%
        Memory 13.8 MB / Beats 69.83%
        """
        col_idx = 0
        row_idx = 0
        direction = [0, 1]
        value = 1

        matrix  = [[0 for j in range(n)] for i in range(n)]
        visited = [[False for j in range(n)] for i in range(n)]
        matrix[0][0] = 1
        visited[0][0] = True

        while value < n*n:
            next_row_idx = row_idx + direction[0]
            next_col_idx = col_idx + direction[1]
            if 0 <= next_col_idx < n and 0 <= next_row_idx < n and not visited[next_row_idx][next_col_idx]:
                visited[next_row_idx][next_col_idx] = True
                value += 1
                matrix[next_row_idx][next_col_idx] = value
                col_idx = next_col_idx
                row_idx = next_row_idx
            else:
                direction[0], direction[1] = direction[1], -direction[0]

        return matrix