class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1],[1,1]]
        
        triangle_list = [[1],[1,1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(1, i):
                row.append(triangle_list[i-1][j-1] + triangle_list[i-1][j]) 
            row.append(1)
            triangle_list.append(row)
        
        return triangle_list