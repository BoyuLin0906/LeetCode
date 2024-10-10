class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        idx_stack = []
        ramp_width = 0

        for idx in range(len(nums)):
            if not idx_stack or nums[idx_stack[-1]] > nums[idx]:
                idx_stack.append(idx)
            else:
                left_idx = 0
                right_idx = len(idx_stack)-1

                while left_idx < right_idx:

                    mid_idx = (left_idx + right_idx) // 2
                    if nums[idx_stack[mid_idx]] > nums[idx]:
                        left_idx = mid_idx+1
                    else:
                        right_idx = mid_idx

                ramp_width = max(ramp_width, idx - idx_stack[right_idx])

        return ramp_width
