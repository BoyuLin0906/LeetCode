"""
Runtime 54 ms / Beats 54.12%
Memory 17.17 MB / Beats 22.00%
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        self.board = [["." for _ in range(n)] for _ in range(n)]
        
        self.n = n
        self.col = set()
        self.left_right_slash = set()
        self.right_left_slash = set()

        self.helper(0)
        return self.result


    def helper(self, row):
        if row == self.n:
            completed_board = [ "".join(r) for r in self.board ]
            self.result.append(completed_board)
            return

        for col in range(self.n):
            if self.is_conflict(row, col):
                continue
            
            left_right_value = row - col
            right_left_value = row + col

            self.col.add(col)
            self.left_right_slash.add(left_right_value)
            self.right_left_slash.add(right_left_value)
            self.board[row][col] = "Q"
            
            self.helper(row+1)
            
            self.board[row][col] = "."
            self.col.remove(col)
            self.left_right_slash.remove(left_right_value)
            self.right_left_slash.remove(right_left_value)


    def is_conflict(self, row, col):
        is_col_conflict = col in self.col

        left_right_value = row - col
        is_left_right_slash_conflict = left_right_value in self.left_right_slash

        right_left_value = row + col
        is_right_left_slash_conflict = right_left_value in self.right_left_slash

        return  is_col_conflict or is_left_right_slash_conflict or is_right_left_slash_conflict