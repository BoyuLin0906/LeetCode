class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        nums_with_idx = list()
        for idx, num in enumerate(nums):
            nums_with_idx.append([num, idx])

        nums_with_idx.sort()

        smaller_oupout = [0] * len(nums)
        for idx in range(len(nums)):
            num = nums_with_idx[idx][0]
            num_idx = nums_with_idx[idx][1]
            if idx > 0 and nums_with_idx[idx-1][0] == num:
                prev_id = nums_with_idx[idx-1][1]
                smaller_oupout[num_idx] = smaller_oupout[prev_id]
            else:
                smaller_oupout[num_idx] = idx

        return smaller_oupout