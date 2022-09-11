class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Runtime: 128 ms, faster than 94.49% of Python3 online submissions for Trapping Rain Water.
        Memory Usage: 16.1 MB, less than 44.85% of Python3 online submissions for Trapping Rain Water.
        """
        # tow pointers
        total = 0
        left_idx = 0
        right_idx = len(height)-1

        while left_idx < right_idx:
            min_height = min(height[left_idx], height[right_idx])
            if min_height == height[left_idx]:
                left_idx += 1
                while left_idx < right_idx and height[left_idx] < min_height:
                    total += min_height - height[left_idx]
                    left_idx += 1
            else:
                right_idx -= 1
                while left_idx < right_idx and height[right_idx] < min_height:
                    total += min_height - height[right_idx]
                    right_idx -= 1
                
        return total