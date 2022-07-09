class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num_length = len(num)
        if num_length == k: return "0"
        # Monotonic Stack
        stack = '0'
        for digit in num:
            while stack[-1] > digit and k:
                stack = stack[:-1]
                k -= 1
            stack += digit
        
        return str(int(stack[:len(stack)-k]))