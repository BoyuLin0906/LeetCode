class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        
        record_rows = [[] for _ in range(numRows)]
        direction, row_idx = 1, 0
        
        for char in s:
            record_rows[row_idx].append(char)
            if row_idx == 0: direction = 1
            elif row_idx == numRows - 1: direction = -1   
            row_idx += direction
        
        return "".join("".join(row) for row in record_rows)