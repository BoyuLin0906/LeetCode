class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = "-" if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0) else ""
        numerator, denominator = abs(numerator), abs(denominator)
        
        remainders = list()
        result = list()
        
        while True:
            result.append(str(numerator // denominator))
            remainder = numerator % denominator
            remainders.append(remainder)
            numerator = remainder * 10
            
            if remainder == 0:
                if len(result) == 1: return sign + result[0]
                return sign + result[0] + '.' + ''.join(result[1:])
            elif remainders.count(remainder) > 1:
                # recurring decimal
                result.insert(remainders.index(remainder)+1, '(')
                result.append(')')
                return sign + result[0] + '.' + ''.join(result[1:])