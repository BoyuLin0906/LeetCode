"""
Runtime : 348 ms, Beats 46.50%
Memory : 23.59 MB, Beats 61.70%
"""

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        idx_stack = []
        ramp_width = 0

        for idx in range(len(nums)):
            if not idx_stack or nums[idx_stack[-1]] > nums[idx]:
                idx_stack.append(idx)
        
        for idx in range(len(nums)-1, -1, -1):
            while idx_stack and nums[idx_stack[-1]] <= nums[idx]:
                popped_idx = idx_stack.pop(-1)
                ramp_width = max(ramp_width, idx - popped_idx)

        return ramp_width