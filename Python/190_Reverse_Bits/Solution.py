class Solution:
    def reverseBits(self, n: int) -> int:
    	"""
    	Runtime: 40 ms, faster than 85.58% of Python3 online submissions for Reverse Bits.
		Memory Usage: 13.8 MB, less than 94.39% of Python3 online submissions for Reverse Bits.
    	"""
        res = 0
        for _ in range(32):
        	# multiply by two
            res = res << 1
            res += (n % 2)
            # divide by two
            n = n >> 1
        return res