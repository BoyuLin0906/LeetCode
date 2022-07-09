class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        interval_len = inter_interval_len = numRows * 2 - 1 - 1
        s_len = len(s)
        
        inter_count = 0
        result = ''
        while inter_interval_len >= 0:
            for idx in range(0, s_len, interval_len):
                if inter_count == 0: result += s[idx]
                elif idx + inter_count < s_len:
                    result += s[idx + inter_count]
                    if inter_interval_len != 0 and idx + inter_count + inter_interval_len < s_len: 
                            result += s[idx + inter_count + inter_interval_len]
            inter_count += 1
            inter_interval_len -= 2
                       
        return result