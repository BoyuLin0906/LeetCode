class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Runtime 76 ms / Beats 83.36%
        Memory 14.6 MB / Beats 8.52%
        """
        stack = []
        for token in tokens:
            print(token)
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                res = self.calculate(num2, num1, token)
                stack.append(res)
        return stack.pop()
    
    def calculate(self, num1, num2, operator):
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            return int(float(num1)/num2)