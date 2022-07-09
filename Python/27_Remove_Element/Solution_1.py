class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        if val not in nums: return len(nums)
        
        val_count = nums.count(val)
        for _ in range(val_count):
            nums.pop(nums.index(val))
        return len(nums)