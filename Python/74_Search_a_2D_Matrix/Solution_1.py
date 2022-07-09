class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearch(row, target):
            left_idx, right_idx = 0, len(row)
            
            while left_idx < right_idx:
                mid_idx = (left_idx + right_idx) // 2
                if target == row[mid_idx]: return True
                elif target > row[mid_idx]: left_idx = mid_idx + 1
                else: right_idx = mid_idx
            return False
            
        for row in matrix:
            if row[0] <= target and row[-1] >= target: return binarySearch(row, target)
                
        return False