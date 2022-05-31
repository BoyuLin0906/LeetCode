class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
    	"""
    	Runtime: 524 ms, faster than 50.00% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
		Memory Usage: 27.2 MB, less than 51.77% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
    	"""
    	# Hashset
        sub_strings = set()
        
        for idx in range(k, len(s)+1):
            sub_strings.add(s[idx-k:idx])
        
        return len(sub_strings) == 2**k