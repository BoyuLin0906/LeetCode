class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        def heapify(tree, tree_length, index):
            left = 2 * index + 1
            right = 2 * index + 2
            _max = index
            
            if left < tree_length and tree[left] > tree[_max]:
                _max = left
            if right < tree_length and tree[right] > tree[_max]:
                _max = right
            
            if _max != index:
                tree[_max], tree[index] = tree[index], tree[_max]
                heapify(tree, tree_length, _max)
            
        def build_heap(tree, tree_length):
            
            last_num = tree_length
            parents_nums = (last_num - 1) // 2
            
            for index in range(parents_nums, -1, -1):
                heapify(tree, last_num, index)
        
        def heap_sort(tree):
            tree_length = len(nums)
            build_heap(nums, tree_length)
            for i in range(tree_length-1, -1, -1):
                nums[0], nums[i] = nums[i], nums[0]
                heapify(nums, i, 0)
                
        heap_sort(nums)