class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    	# (total!) / a! * b! * c! ...
    	# steps: m-1 & n-2
    	# ((m-1) + (n-1))! / (m-1)! * (n-1)!
        return int(math.factorial(m+n-2) / (math.factorial(m-1) * math.factorial(n-1)))