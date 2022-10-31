class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
		Runtime: 37 ms, faster than 87.22% of Python3 online submissions for Pascal's Triangle II.
		Memory Usage: 13.8 MB, less than 64.93% of Python3 online submissions for Pascal's Triangle II.
        """
        ret = [1] * (rowIndex+1)
        
        upper_value = rowIndex
        lower_value = 1
        for row_idx in range(1, rowIndex):
            ret[row_idx] = ret[row_idx-1] * upper_value // lower_value
            upper_value -= 1
            lower_value += 1
            
        return ret