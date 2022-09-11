class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Runtime: 136 ms, faster than 90.40% of Python3 online submissions for Trapping Rain Water.
        Memory Usage: 16.1 MB, less than 44.85% of Python3 online submissions for Trapping Rain Water.
        """
        # tow pointers
        total = 0
        left_idx = 0
        right_idx = len(height)-1
        temp_height = 0

        while left_idx < right_idx:
            min_height = min(height[left_idx], height[right_idx])
            
            if min_height == height[left_idx]: left_idx += 1
            else: right_idx -= 1
                
            temp_height = max(temp_height, min_height)
            total += temp_height - min_height

                
        return total