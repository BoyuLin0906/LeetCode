class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    	# convert list to string
        number = ""
        for digit in digits:
            number += str(digit)
        digits = []
        # after plus one, string convert to integer
        for _str in str(int(number) + 1):
            digits.append(int(_str))
        return digits