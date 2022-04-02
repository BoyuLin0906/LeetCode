class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        tagert_num = n * 2
        result = []
        
        def generate(cur_parenthesis, opne_count, close_count):
            if len(cur_parenthesis) == tagert_num:
                result.append(cur_parenthesis)
                return
            if opne_count < n: 
                generate(cur_parenthesis + "(", opne_count + 1, close_count)
            if close_count < opne_count: 
                generate(cur_parenthesis + ")", opne_count, close_count + 1)
    
        generate("", 0, 0)
        return result
                    