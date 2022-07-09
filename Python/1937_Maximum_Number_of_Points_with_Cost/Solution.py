class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        X X X X
        X X X X
        X X X X
        X X X X
        
        Need to compare both sides(from left and from right) to find the maximum
        [e.g]
        4 2 1 6
        4 3 2 6 (from left)
        4 4 5 6 (from right)
        4 4 5 6 (combine both)

        (1)
        max points
        M M M M -> X X X X

        X X X X
        X X X X
        X X X X
        
        (2)
        max points
        M M M M -> X X X X
                   X X X X

        X X X X
        X X X X

        (3)
        max points
        M M M M -> X X X X
                   X X X X
                   X X X X

        X X X X

        (3)
        max points
        M M M M -> X X X X
                   X X X X
                   X X X X
                   X X X X
        """
        column_length, row_length = len(points), len(points[0])
        dp = points[0]
        
        for column in range(1, column_length):
            left = [dp[0]] + [0] * (row_length-1)
            right = [0] * (row_length-1) + [dp[-1]]

            # from left
            for row in range(row_length): 
                left[row] = max(left[row - 1] - 1, dp[row])

            # from right
            for row in range(row_length-2, -1, -1): 
                right[row] = max(right[row + 1] - 1, dp[row])

            # save in dp
            for row in range(row_length): 
                dp[row] = points[column][row] + max(left[row], right[row])
            
        return max(dp)