class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Runtime: 141 ms, faster than 28.49% of Python3 online submissions for N-Queens.
        Memory Usage: 14.4 MB, less than 82.08% of Python3 online submissions for N-Queens.
        """
        # DFS + backtracking
        result = []
        
        def is_conflict(board, row, col):
            for r in range(row):
                if abs(col - board[r]) in (row - r, 0): return True
            return False
        
        def create_queen(board, row):
            if row == n: 
                result.append(["." * col + "Q" + "." * (n - col - 1) for col in board])
                return 
                
            for col in range(n):
                if not is_conflict(board, row, col):
                    board[row] = col
                    create_queen(board, row + 1)
                    
        create_queen([-1] * n, 0)
        return result           