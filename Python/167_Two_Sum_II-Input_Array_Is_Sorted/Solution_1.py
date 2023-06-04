class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Runtime 129 ms / Beats 85.36%
        Memory 17.4 MB / Beats 11.63%
        """
        # two pointer
        left, right = 0, len(numbers)-1

        while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum == target:
                return [left+1, right+1]
            elif two_sum > target:
                right -= 1
            else:
                left += 1