"""
Runtime 50 ms / Beats 85.52%
Memory 16.58 MB / Beats 89.73%
"""
from collections import Counter

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        counter = Counter()
        counter[0] = 1

        max_or = 0
        for num in nums:

            for total, count in list(counter.items()):
                counter[total | num] += count
            max_or |= num

     
        return counter[max_or]
"""
input -> [3,1,1,4,7]

3
Counter({0: 1, 3: 1})
1
Counter({3: 2, 0: 1, 1: 1})
1
Counter({3: 4, 1: 3, 0: 1})
4
Counter({3: 4, 7: 4, 1: 3, 5: 3, 0: 1, 4: 1})
7
Counter({7: 20, 3: 4, 1: 3, 5: 3, 0: 1, 4: 1})

"""