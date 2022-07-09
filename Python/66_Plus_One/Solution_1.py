class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # list method 
        digits.reverse()
        for i in range(len(digits)):
            digits[i] = (digits[i] + 1) % 10
            if digits[i] != 0: 
                break
            if i+1 == len(digits):
                digits.append(1)

        digits.reverse()  
        return digits