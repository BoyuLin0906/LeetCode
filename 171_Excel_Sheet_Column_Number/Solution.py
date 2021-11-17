class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        len_str = len(columnTitle) 
        # ord(letter) - 64
        columnTitle = columnTitle[::-1]
        result = 0
        for i in range(len_str):
            result += (ord(columnTitle[i]) - 64) * (26**i)
        return result