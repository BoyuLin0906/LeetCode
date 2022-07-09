class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        length = len(height)
        left_p, right_p = 0, length-1
        max_water = 0
        
        while left_p < right_p:
            max_water = max(max_water, min(height[left_p], height[right_p]) * (right_p-left_p))
            if height[left_p] <= height[right_p]:
                left_p += 1
            else:
                right_p -= 1
                
        return max_water