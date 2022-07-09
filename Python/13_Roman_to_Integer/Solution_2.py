class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        if len(s) == 1: return roman_num[s]
        
        roman_combine_num = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        if len(s) == 2 and s in roman_combine_num : 
            return roman_combine_num[s]
        elif len(s) == 2:
            return roman_num[s[0]] + roman_num[s[1]]
        
        _sum = 0
        _index = 0
        while _index < len(s):
            # ckeck 'roman_combine_num' table
            if s[_index:_index+2] in roman_combine_num.keys():
                _sum += roman_combine_num[s[_index:_index+2]]
                _index += 2
            # ckeck 'roman_num' table
            else:
                _sum += roman_num[s[_index]]
                _index += 1
            if _index >= len(s):
                break
        
        return _sum