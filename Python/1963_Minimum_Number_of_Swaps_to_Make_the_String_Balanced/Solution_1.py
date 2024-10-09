class Solution:
    def minSwaps(self, s: str) -> int:
        
        stack = []
        for char in s:
            if stack and stack[-1] == "[" and char == "]":
                stack.pop(-1)
            else:
                stack.append(char)

        count = len(stack) // 4
        if len(stack) % 4 != 0:
            count += 1
            
        return count