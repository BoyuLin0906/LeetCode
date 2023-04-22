class Solution:
    def generateMatrix(self, n):
        """
        Runtime 28 ms / Beats 90.50%
        Memory 13.9 MB / Beats 25.29%
        """
        matrix, low_value = [[]], n*n+1

        while low_value > 1:
            # step1. 9
            # step2. 8
            # step3. 7, 6
            # step4. 5, 4
            # step5. 3, 2, 1
            high_value = low_value
            low_value = low_value - len(matrix)
            # reverse internal list, concatenate the internal list
            matrix = list(zip(*matrix[::-1]))
            # add new values
            matrix = [[v for v in range(low_value, high_value)]] + matrix
        return matrix