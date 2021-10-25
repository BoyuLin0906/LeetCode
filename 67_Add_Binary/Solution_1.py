class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        
        a_len, b_len = len(a), len(b) 
        a_index, b_index = 0, 0
        carry = 0
        result = ""
        
        while a_index < a_len or b_index < b_len or carry:
            temp_val = 0
            
            if a_index < a_len:
                temp_val += int(a[a_index])
                a_index += 1
                
            if b_index < b_len:
                temp_val += int(b[b_index])
                b_index += 1
            
            temp_val += carry
            
            carry = temp_val // 2
            temp_val = temp_val % 2
            result += str(temp_val)
        
        return result[::-1]