class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
        Runtime: 21 ms, faster than 99.74% of Python3 online submissions for Excel Sheet Column Title.
        Memory Usage: 13.9 MB, less than 55.61% of Python3 online submissions for Excel Sheet Column Title.
        """
        char_map = [chr(i) for i in range(65,91)]
        res = ""
        
        while columnNumber:
            res += char_map[(columnNumber -1) % 26]
            columnNumber = (columnNumber - 1) // 26
            
        return res[::-1]