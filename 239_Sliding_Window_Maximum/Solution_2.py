class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if not nums: return nums
        
        nums_length = len(nums) 
        left_nums, right_nums = [0] * nums_length, [0] * nums_length
        
        for idx in range(0, nums_length, k):
            range_idx = nums_length if idx+k > nums_length else idx+k
            # left
            max_value = -100000
            for block_idx in range(idx, range_idx):
                #print(block_idx)
                if max_value < nums[block_idx]: max_value = nums[block_idx]
                left_nums[block_idx] = max_value
            
            # right
            max_value = -100000
            for block_idx in range(range_idx-1, idx-1, -1):
                if max_value < nums[block_idx]: max_value = nums[block_idx]
                right_nums[block_idx] = max_value
        
        result = []
        for idx in range(0, nums_length-k+1):
            result.append(max(left_nums[k+idx-1],right_nums[idx]))
        
        return result