"""
Runtime 49 ms / Beats 81.96%
Memory 17.10 MB / Beats 42.40%
"""

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        decompressed_list = list()
        for idx in range(0, len(nums), 2):
            freq = nums[idx]
            val = nums[idx+1]
            sub_list = [val] * freq
            decompressed_list += sub_list
        
        return decompressed_list