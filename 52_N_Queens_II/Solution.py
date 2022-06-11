class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        Runtime: 63 ms, faster than 71.89% of Python3 online submissions for N-Queens II.
        Memory Usage: 14 MB, less than 16.07% of Python3 online submissions for N-Queens II.
        """
        # DFS + backtracking + direction restrict
        total_count = 0
        board = [["."] * n for i in range(n)]

        col_set = set()
        right_left_set = set() # row + col
        left_right_set = set() # row - col 
        
        def create_queen(row):
            if row == n:
                return 1
            
            count = 0
            for col in range(n):
                rc_sum = row + col
                rc_diff = row - col
                if (not col in col_set and not rc_sum in right_left_set and not rc_diff in left_right_set):
                    # add in restrict
                    col_set.add(col)
                    right_left_set.add(rc_sum)
                    left_right_set.add(rc_diff)
                    board[row][col] = "Q"
                    
                    count += create_queen(row + 1)
                    
                    # reset in restrict
                    col_set.remove(col)
                    right_left_set.remove(rc_sum)
                    left_right_set.remove(rc_diff)
                    board[row][col] = "."
            return count
                    
        total_count = create_queen(0)
        return total_count