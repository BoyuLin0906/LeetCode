class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = "-" if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0) else ""
        numerator, denominator = abs(numerator), abs(denominator)
        
        remainders = defaultdict(lambda: 0)
        result = list()
        index = 1
        
        while True:
            result.append(str(numerator // denominator))
            remainder = numerator % denominator
            
            if remainder == 0:
                if len(result) == 1: return sign + result[0]
                return sign + result[0] + '.' + ''.join(result[1:])
            elif remainders[remainder]:
                print(result)
                # recurring decimal
                result.insert(remainders[remainder], '(')
                result.append(')')
                return sign + result[0] + '.' + ''.join(result[1:])
            
            remainders[remainder] = index
            numerator = remainder * 10
            index += 1