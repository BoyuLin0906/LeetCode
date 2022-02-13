class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        current_sum = 0
        total_number = 0
        sum_frequency = {0 : 1}
        
        for num in nums:
            current_sum += num
            diff_num = current_sum - k
            
            total_number += sum_frequency.get(diff_num, 0) 
            sum_frequency[current_sum] = 1 + sum_frequency.get(current_sum, 0)
        
        return total_number