class Solution:
    def maximum69Number (self, num: int) -> int:
        """
        Runtime 32 ms / Beats 93.8%
        Memory 13.9 MB / Beats 9.69%
        """
        tmp_num = num
        count = 0
        changed_digit = -1

        while tmp_num:
            mod_num = tmp_num % 10
            if mod_num == 6: 
                changed_digit = count
            count += 1  
            tmp_num //= 10

        if changed_digit != -1:
            num += 3 * (10**changed_digit)

        return num