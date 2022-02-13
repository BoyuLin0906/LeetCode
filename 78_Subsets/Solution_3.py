class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_length = len(nums)
        subsets_result = [[]]
        
        def find(index, result):
            if nums_length > index:
                for x in [item + [nums[index]] for item in result]: 
                    result.append(x)
                find(index+1, result)
                
        find(0, subsets_result)
        return subsets_result