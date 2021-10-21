class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {1:1, 2:2}
        if n in mem:
            return n
        for i in range(3, n+1):
            mem[i] = mem[i-1] + mem[i-2]

        return mem[n]