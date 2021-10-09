class Solution:
    def reverse(self, x: int) -> int:
        if x==0 or x < -2**31 or x > (2**31) - 1: 
            return 0
        # reverse string
        x = str(x)[::-1]
        # minus sgin
        if "-" in x: x = "-" + x[:-1]
        # string to integer, it can delete unnecessary '0'
        x = int(x)
        if x < -2**31 or x > (2**31)-1: 
            return 0
        return x