class Solution:
    def summaryRanges(self, nums):
        result = []

        for num in nums:
            if not result or num > result[-1][-1] + 1:
                result += [[]]
            # repalce list after index 0
            result[-1][1:] = [num]
            
        return ['->'.join(map(str, r)) for r in result]