class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        """
        Runtime: 1858 ms, faster than 90.00% of Python3 online submissions for Earliest Possible Day of Full Bloom.
        Memory Usage: 31.7 MB, less than 58.71% of Python3 online submissions for Earliest Possible Day of Full Bloom.
        """
        # sort
        times = list()
        flowers_number = len(plantTime)
        
        for idx in range(flowers_number):
            times.append((plantTime[idx], growTime[idx]))
        # sort by grow time
        times.sort(key=lambda x:x[1], reverse=True)
        
        result = 0
        days = 0
        # plant the longest growing flowers first
        for idx in range(flowers_number):
            days += times[idx][0]
            result = max(result, days+times[idx][1])
        
        return result