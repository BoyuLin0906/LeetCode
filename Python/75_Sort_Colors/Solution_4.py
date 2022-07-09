class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        def merge_sort(_list):
            if len(_list) == 1: return _list
            # divide
            length = len(_list)
            left_list = _list[0:(length//2)]
            right_list = _list[(length//2):length]
            left_list = merge_sort(left_list)
            right_list = merge_sort(right_list)
            
            return merge(left_list, right_list)
        
        def merge(left_list, right_list):
            temp_list = []
            while left_list and right_list:
                if left_list[0] < right_list[0]:
                    temp_list.append(left_list.pop(0))
                else:
                    temp_list.append(right_list.pop(0))
                    
            if left_list: temp_list += left_list
            if right_list: temp_list += right_list
            
            return temp_list
        
        _list = merge_sort(nums)
        for i in range(len(nums)):
            nums[i] = _list[i]
        
        print(nums)