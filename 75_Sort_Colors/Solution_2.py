class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Quick Sort
        def quicksort(data, left, right):
            if left >= right : return
            
            sub_left, sub_right = left, right
            pivot = data[left]

            while sub_left != sub_right:
                # search smaller than pivot
                while data[sub_right] > pivot and sub_left < sub_right:
                    sub_right -= 1
                # search greater than or equal to pivot
                while data[sub_left] <= pivot and sub_left < sub_right:
                    sub_left += 1
                # exchange
                if sub_left < sub_right:
                    data[sub_right], data[sub_left] = data[sub_left], data[sub_right]
            
            # pivot to correct position
            data[left] = data[sub_left] 
            data[sub_left] = pivot

            # left
            quicksort(data, left, sub_right-1)
            # right
            quicksort(data, sub_left+ 1, right)
            
        quicksort(nums, 0, len(nums)-1)