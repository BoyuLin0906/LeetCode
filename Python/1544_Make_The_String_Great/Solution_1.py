class Solution:
    def makeGood(self, s: str) -> str:
    	"""
		Runtime 45 ms / Beats 83.32%
		Memory 13.8 MB / Beats 97.60%
    	"""
    	# recursion
        find_idx = -1
        for idx in range(len(s)-1):
            if abs(ord(s[idx])-ord(s[idx+1])) == 32:
                find_idx = idx
                break
        
        if find_idx > -1:
            s = self.makeGood(s[:find_idx] + s[find_idx+2:])

        return s