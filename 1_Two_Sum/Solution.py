from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        
        # create dictionary
        for _index in range(len(nums)):
            nums_dict[nums[_index]] = _index
        
        # get indexes
        for _index in range(len(nums)):
            if target - nums[_index] in nums_dict:
                if nums_dict[target - nums[_index]] != _index:
                    return [_index, nums_dict[target - nums[_index]]]
        return []
    


