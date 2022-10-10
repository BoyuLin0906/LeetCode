class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Runtime: 337 ms, faster than 95.35% of Python3 online submissions for Longest Consecutive Sequence.
        Memory Usage: 29 MB, less than 61.29% of Python3 online submissions for Longest Consecutive Sequence.
        """
        nums_set = set(nums)
        longest_length = 0
        
        for num in nums_set:
            # skip if the bigger number exists
            if num + 1 in nums_set: continue
            
            # count the consecutive sequence
            count = 1
            while num - count in nums_set:
                count += 1
            
            longest_length = max(longest_length, count)
            
        return longest_length