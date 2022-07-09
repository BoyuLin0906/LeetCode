# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start_num = 1
        mid_num = 0
        # binary search
        while start_num <= n:
            mid_num = int((start_num+n)/2)
            status = guess(mid_num)
            if status == 0:
                return mid_num
            elif status == -1:
                n = mid_num - 1
            elif status == 1:
                start_num = mid_num + 1