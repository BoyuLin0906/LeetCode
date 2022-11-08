class Solution:
    def makeGood(self, s: str) -> str:
        """
		Runtime 37 ms / Beats 94.53%
		Memory 13.9 MB / Beats 15.6%
        """
        # stack
        stack = []
        for char in s:
            if stack and abs(ord(char)-ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)