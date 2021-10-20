class Solution:
    def mySqrt(self, x: int) -> int:
        low_value = 0
        high_value = x
        ans = 0
        while low_value <= high_value:
            middle_value = (low_value + high_value) // 2
            target = middle_value*middle_value
            if target == x:
                return middle_value
            if target > x:
                high_value = middle_value - 1
            else:
                ans = middle_value
                low_value = middle_value + 1
        return ans