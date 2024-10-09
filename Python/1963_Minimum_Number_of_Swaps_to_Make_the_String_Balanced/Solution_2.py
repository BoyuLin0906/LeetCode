class Solution:
    def minSwaps(self, s: str) -> int:
        
        size = 0
        for char in s:
            if char == "[":
                size += 1
            elif size > 0:
                size -= 1

        swap_count = (size + 1) // 2
        return swap_count