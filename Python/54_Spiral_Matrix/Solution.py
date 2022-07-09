class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        result = []
        upper_idx, left_idx = 0, 0
        right_idx, lower_idx = len(matrix[0])-1, len(matrix)-1
        
        while left_idx <= right_idx and upper_idx <= lower_idx:
            # right
            for idx in range(left_idx, right_idx+1): result.append(matrix[upper_idx][idx])
            upper_idx += 1
            
            # down
            for idx in range(upper_idx, lower_idx+1): result.append(matrix[idx][right_idx])
            right_idx -= 1
            
            if left_idx > right_idx or upper_idx > lower_idx: break
            
            # left
            for idx in range(right_idx, left_idx-1, -1): result.append(matrix[lower_idx][idx])
            lower_idx -= 1
            
            # up
            for idx in range(lower_idx, upper_idx-1, -1): result.append(matrix[idx][left_idx])
            left_idx += 1
            
        return result