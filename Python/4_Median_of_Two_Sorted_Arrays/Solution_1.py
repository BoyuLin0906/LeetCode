class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        num1_len, num2_len = len(nums1), len(nums2)
        sum_len = num1_len + num2_len
        mid_count = sum_len // 2
        count = 0
        temp = list()
        
        while count < mid_count+1:
            if nums1 and nums2:
                if nums1[-1] > nums2[-1]: temp.append(nums1.pop())
                else: temp.append(nums2.pop())
            elif nums1: temp.append(nums1.pop())
            else: temp.append(nums2.pop())
            count += 1
        
        if sum_len % 2: return float(temp[-1])
        else:  return sum(temp[-2:])/2