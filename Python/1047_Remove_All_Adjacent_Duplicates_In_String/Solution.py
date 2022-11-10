class Solution:
    def removeDuplicates(self, s: str) -> str:
    	"""
		Runtime 90 ms / Beats 88.3%
		Memory 14.8 MB / Beats 52.58%
    	"""
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)