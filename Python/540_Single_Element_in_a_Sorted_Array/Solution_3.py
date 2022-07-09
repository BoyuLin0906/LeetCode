class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums)-1
        # binary search
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] == nums[mid+1]:
                if mid % 2 == 0:
                    left = mid + 2
                else:
                    right = mid - 1
            elif nums[mid] == nums[mid-1]:
                if mid % 2 == 0:
                    right = mid - 2
                else:
                    left = mid + 1
            else:
                return nums[mid]

        return nums[left]