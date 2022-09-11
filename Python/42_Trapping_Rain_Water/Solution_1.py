class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Runtime: 139 ms, faster than 88.86% of Python3 online submissions for Trapping Rain Water.
        Memory Usage: 16 MB, less than 44.85% of Python3 online submissions for Trapping Rain Water.
        """
        # monotonic stack
        total = 0
        stack = list()
        n = len(height)
        idx = 0
        
        while idx < n:
            if not stack or height[stack[-1]] > height[idx]:
                stack.append(idx)
                idx += 1
            else:
                pop_idx = stack.pop()
                # do not have trough
                if not stack: continue
                    
                trough_height = min(height[stack[-1]], height[idx]) - height[pop_idx]
                trough_width = (idx - 1) - stack[-1] 
                total += trough_height * trough_width
                
        return total