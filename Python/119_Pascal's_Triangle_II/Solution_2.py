class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        Runtime: 37 ms, faster than 87.22% of Python3 online submissions for Pascal's Triangle II.
		Memory Usage: 13.8 MB, less than 64.93% of Python3 online submissions for Pascal's Triangle II.
        """
        ret = [1] * (rowIndex+1)
        for row_idx in range(2, rowIndex+1):
            for col_idx in range(row_idx-1, 0, -1):
                ret[col_idx] += ret[col_idx-1] 
            
        return ret