class Solution:
    def calculate(self, s: str) -> int:
        """
        Runtime 110 ms / Beats 86.95%
        Memory 15.4 MB / Beats 55.19%
        """
        # stack
        stack, num, sign = [0], 0, 1

         for char in s:
            # pass blank char
            if char == " ": 
                continue
            # create integer
            if char.isdigit():
                num = (num * 10) + int(char)
            # add prev number and reset to poitive sign
            if char == "+":
                stack[-1] += num * sign
                sign, num = 1, 0
            # add prev number and reset to negative sign
            elif char == "-":
                stack[-1] += num * sign
                sign, num = -1, 0
            # remain prev number and reset them
            elif char == "(":
                stack.append(sign)
                stack.append(num)
                sign, num = 1, 0
            # add prev number and last number
            elif char == ")":
                pre_value, pre_sign = stack.pop(), stack.pop()
                last_num = (pre_value + num * sign) * pre_sign
                stack[-1] += last_num
                sign, num = 1, 0

        return stack[-1] + num * sign