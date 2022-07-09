class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {
            "0": 0,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        if len(s) == 1: return roman_num[s]
        
        _cur = "0"
        _pre = "0"
        _sum = 0
        # reversed string of Roman numerals
        for _str in reversed(s):
            _cur = _str
            if roman_num.get(_cur) < roman_num.get(_pre):
                # if previous symbol is bigger than current symbol,
                # it means IX = 9, XL = 40 ... etc 
                _sum -= roman_num.get(_cur)
            else:
                # add current numerals
                _sum += roman_num.get(_cur)
            _pre = _cur
        return _sum