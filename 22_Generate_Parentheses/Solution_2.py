class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        tagert_num = n * 2
        result = []
        stack = [("", 0, 0)]
        
        while stack:
            cur_parenthesis, opne_count, close_count = stack.pop()
            if len(cur_parenthesis) == tagert_num:
                result.append(cur_parenthesis)
            else:
                if opne_count < n:
                    stack.append((cur_parenthesis + "(", opne_count + 1, close_count))
                if close_count < opne_count: 
                    stack.append((cur_parenthesis + ")", opne_count, close_count + 1))
        
        return result