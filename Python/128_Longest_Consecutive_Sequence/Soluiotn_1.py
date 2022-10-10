class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Runtime: 505 ms, faster than 79.33% of Python3 online submissions for Longest Consecutive Sequence.
        Memory Usage: 29 MB, less than 28.79% of Python3 online submissions for Longest Consecutive Sequence.
        """
        nums_set = set(nums)
        longest_length = 0
        
        for num in nums:
            count = 1
            temp_len = 1
            # find backward
            while num - temp_len in nums_set:
                nums_set.remove(num - temp_len)
                count += 1
                temp_len += 1
                
            temp_len = 1
            # find forward
            while num + temp_len in nums_set:
                nums_set.remove(num + temp_len)
                count += 1
                temp_len += 1
            
            longest_length = max(longest_length, count)
            
        return longest_length