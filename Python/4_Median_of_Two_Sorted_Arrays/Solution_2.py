class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        num1_len, num2_len = len(nums1), len(nums2)
        num1 = num2 = None
        idx1 = idx2 = 0
        count = 0
        
        while count < ((num1_len + num2_len) // 2) + 1:
            num2 = num1
            if idx2 == num2_len or (idx1 != num1_len and nums1[idx1] <= nums2[idx2]):
                num1 = nums1[idx1]
                idx1 += 1
            else:
                num1 = nums2[idx2]
                idx2 += 1
            count += 1
            
        return float(num1) if (num1_len + num2_len) % 2 else (num2 + num1) / 2