class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        result = 0
        # integer is 32-bit, two complement binary.
        # In python, the signs of the numbers have the parameter 'nega' to save.
        # So, we can't use the result which is negative immediately.
        # reference:
        #   1. https://www.ele.uri.edu/courses/ele447/proj_pages/divid/twos.html?pagewanted=all
        #   2. https://stackoverflow.com/questions/2654149/bit-length-of-a-positive-integer-in-python
        #   3. https://realpython.com/python-bitwise-operators/

        for shift_size in range(32):
            bit_sum = 0
            for num in nums:
                bit_sum += (num >> shift_size) & 1
                
            bit_sum = bit_sum % 3
            bit_sum = bit_sum << shift_size
            result |= bit_sum
        
        # check result if it is negative
        if ( result & (1 << 31) ) == 0:
            return result
        else:
            # convert to negative number 
            return -((result ^ (0xFFFFFFFF))+1)