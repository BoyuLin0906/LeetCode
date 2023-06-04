class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    	"""
    	Runtime 238 ms / Beats 5.3%
		Memory 17.3 MB / Beats 38.66%
    	"""
    	# binary search
        num_len = len(numbers)
        for i in range(num_len):
            diff = target-numbers[i]
            low = 0
            high = num_len-1

            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == diff and i != mid:
                    return [i+1, mid+1]
                elif numbers[mid] > diff:
                    high = mid-1
                else:
                    low = mid+1