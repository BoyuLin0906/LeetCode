class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
		Runtime: 99 ms, faster than 98.23% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
		Memory Usage: 18.7 MB, less than 39.82% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
        """
        str_stack = [["$", 0]]
        
        for char in s:
            if str_stack[-1][0] == char:
                str_stack[-1][1] += 1
                if str_stack[-1][1] == k: str_stack.pop()
            else:
                str_stack.append([char, 1])
                    
        return "".join(char * count for char, count in str_stack)