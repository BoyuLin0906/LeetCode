class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2: return False
        
        parentheses_table = {"(": ")", "{": "}", "[": "]"}       
        stack_list = []
        for _str in s:
            if _str in parentheses_table.keys():
                stack_list.append(_str)
            else:
                if not stack_list or parentheses_table[stack_list.pop()] != _str:
                    return False
        return stack_list == []