class Solution:
    def isPalindrome(self, x: int) -> bool:
    	# integer to string
        x = str(x)
        # check whether string and reverse string are equal
        if x == x[::-1]:
            return True
        return False