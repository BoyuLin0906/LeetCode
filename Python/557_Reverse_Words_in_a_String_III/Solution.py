class Solution:
    def reverseWords(self, s: str) -> str:
    	"""
    	Runtime 27 ms / Beats 97.14%
		Memory 14.4 MB / Beats 96.38%
    	"""
        word_list = s.split(' ')
        word_len = len(word_list)

        for idx in range(word_len):
            word_list[idx] = word_list[idx][::-1]

        return " ".join(word_list)