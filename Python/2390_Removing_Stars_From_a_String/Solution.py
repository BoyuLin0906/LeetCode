class Solution:
    def removeStars(self, s: str) -> str:
    	"""
		Runtime 309 ms / Beats 84.97%
		Memory 15.7 MB / Beats 20.97%
    	"""
        stack = []

        for char in s:
            if stack and char[-1] == "*":
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)