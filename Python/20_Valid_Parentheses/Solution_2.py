class Solution:
    def isValid(self, s: str) -> bool:
        
        parentheses_table = {"(": ")", "{": "}", "[": "]"}       
        stack_str = ""
        for _str in s:
            if _str in parentheses_table.keys():
                stack_str += _str
            else:
                if stack_str and parentheses_table[stack_str[-1]] == _str:
                    stack_str = stack_str[:-1]
                else:
                    return False
        if stack_str != "":
            return False
        return True