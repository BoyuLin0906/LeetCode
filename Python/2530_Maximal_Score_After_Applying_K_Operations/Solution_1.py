"""
Runtime 742 ms / Beats 39.24%
Memory 31.05 MB / Beats 92.09%
"""
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)
        
        max_score = 0
        for _ in range(k):
            num = heapq.heappop(nums)
            num = -num
            max_score += num

            replaced_num = 0
            if num % 3 != 0:
                replaced_num += 1
            replaced_num += num // 3
            
            heapq.heappush(nums, -replaced_num)

        return max_score