import math
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        """
		Runtime 1608 ms / Beats 85.56%
		Memory 30.5 MB / Beats 72.41%
        """
        stack = []
        for num in nums:
            while stack and math.gcd(num, stack[-1]) > 1:
                pop_num = stack.pop()
                num = math.lcm(num, pop_num)
            stack.append(num)
        return stack