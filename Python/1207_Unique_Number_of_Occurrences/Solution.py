from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
    	"""
		Runtime 44 ms / Beats 83.82%
		Memory 13.9 MB / Beats 97.26%
    	"""
        counters = Counter(arr)
        return len(set(counters.values())) == len(set(counters.keys()))