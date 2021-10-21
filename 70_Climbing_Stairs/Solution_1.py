class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1,2] + [0] * (n-2)
        
        for i in range(0, len(steps)-2):
            steps[i+2] = steps[i] + steps[i+1]
        
        return steps[n-1]