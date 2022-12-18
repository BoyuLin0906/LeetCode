class Solution:
    def halvesAreAlike(self, s: str) -> bool:
    	"""
		Runtime 33 ms / Beats 96.36%
		Memory 13.9 MB / Beats 75%
    	"""
        half_len = len(s)//2
        rules = "AEIOUaeiou"
        head_count = 0
        tail_count = 0

        for idx in range(half_len):
            if s[idx] in rules: head_count += 1
            if s[idx + half_len] in rules: tail_count += 1
        
        return head_count == tail_count