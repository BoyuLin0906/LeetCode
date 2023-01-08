class Solution:
    def detectCapitalUse(self, word: str) -> bool:
    	"""
    	Runtime 26 ms / Beats 95.66%
		Memory 13.9 MB / Beats 49.27%
    	"""
        return len(word) == 1 or word[1:].islower() or word.isupper()