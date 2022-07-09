class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return nums
        
        result = []
        left_idx, right_idx = 0, 0
        nums_length = len(nums)
        
        while left_idx < nums_length - 1 and right_idx < nums_length - 1:
            if nums[right_idx] + 1 != nums[right_idx + 1]:
                result.append([nums[left_idx], nums[right_idx]] if left_idx != right_idx else [nums[left_idx]])
                left_idx = right_idx + 1
            right_idx += 1
        # add finally range
        result.append([nums[left_idx], nums[right_idx]] if left_idx != right_idx else [nums[left_idx]])
        return ['->'.join(map(str, r)) for r in result]