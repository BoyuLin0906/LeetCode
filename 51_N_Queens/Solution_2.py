class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Runtime: 61 ms, faster than 86.54% of Python3 online submissions for N-Queens.
        Memory Usage: 14.4 MB, less than 43.55% of Python3 online submissions for N-Queens.
        """
        # DFS + backtracking + direction restrict
        result = []
        board = [["."] * n for i in range(n)]

        col_set = set()
        right_left_set = set() # row + col
        left_right_set = set() # row - col 
        
        def create_queen(row):
            if row == n:
                result.append(["".join(row) for row in board])
                return 
            
            for col in range(n):
                rc_sum = row + col
                rc_diff = row - col
                if (not col in col_set and not rc_sum in right_left_set and not rc_diff in left_right_set):
                    # add in restrict
                    col_set.add(col)
                    right_left_set.add(rc_sum)
                    left_right_set.add(rc_diff)
                    board[row][col] = "Q"
                    
                    create_queen(row + 1)
                    
                    # reset in restrict
                    col_set.remove(col)
                    right_left_set.remove(rc_sum)
                    left_right_set.remove(rc_diff)
                    board[row][col] = "."
                    
        create_queen(0)
        return result