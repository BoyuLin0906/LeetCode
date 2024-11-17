"""
Runtime 47 ms / Beats 30.00%
Memory 16.79 MB / Beats 56.34%
"""

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        window = []
        for idx in range(k):
            window.append(nums[idx])
        
        res = [-1]
        if self.check_consecutive(window):
            res[0] = window[-1]

        for idx in range(k, len(nums)):

            window.pop(0)
            window.append(nums[idx])

            if self.check_consecutive(window):
                res.append(window[-1])
            else:
                res.append(-1)

        return res

    def check_consecutive(self, stack):
        for idx in range(1, len(stack)):
            if stack[idx] - stack[idx-1] != 1:
                return False
        return True