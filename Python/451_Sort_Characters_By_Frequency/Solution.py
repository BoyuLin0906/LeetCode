from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
    	"""
		Runtime 56 ms / Beats 85.34%
		Memory 15.3 MB / Beats 49.59%
    	"""
        counter = Counter(s)
        s_len = len(counter)

        res_s = "" 
        for char, count in counter.most_common(s_len):
            for _ in range(count):
                res_s += char 
        
        return res_s