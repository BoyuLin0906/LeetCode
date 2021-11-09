class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        result = set()
        nums = list(counter.keys())
        
        if counter[0] >= 3: result.add((0, 0, 0))
        positive_nums = [x for x in nums if x > 0]
        negative_nums = [x for x in nums if x < 0]
        
        for positive_num in positive_nums:
            for negative_num in negative_nums:
                num = 0 - (negative_num + positive_num)
                if (num in counter and (positive_num != num and negative_num != num)) or counter[num] >= 2:
                    result.add(tuple(sorted([num, positive_num, negative_num])))
        
        return [list(i) for i in result]