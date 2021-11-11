class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1],[1,1]]
        
        p_tri_list = self.generate(numRows-1)
        pre_list = p_tri_list[numRows-2]
        
        cur_list = [1]
        for i in range(1, numRows-1):
            cur_list.append(pre_list[i-1] + pre_list[i])
        cur_list.append(1)
        p_tri_list.append(cur_list)
        
        return p_tri_list