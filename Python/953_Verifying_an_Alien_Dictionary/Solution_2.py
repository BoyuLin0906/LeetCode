class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
    	"""
    	Runtime 55 ms / Beats 26.18%
		Memory 14 MB / Beats 31.27%
    	"""
        sorted_words = sorted(words, key=lambda word:[order.index(c) for c in word])
        return words == sorted_wrods