class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        column_len, row_len = len(matrix), len(matrix[0])
        left_idx, right_idx = 0, column_len * row_len
        
        while left_idx < right_idx:
            mid_idx = (left_idx + right_idx) // 2
            print(mid_idx)
            mid_value = matrix[mid_idx//row_len][mid_idx%row_len]

            if target == mid_value: return True
            elif target > mid_value: left_idx = mid_idx + 1
            else: right_idx = mid_idx
                
        return False