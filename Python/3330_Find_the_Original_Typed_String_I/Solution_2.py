class Solution:
    def possibleStringCount(self, word: str) -> int:
        """
        Runtime 38 ms / Beats 67.51
        Memory 17.77 MB / Beats 46.78%
        """
        word_len = len(word)
        total = word_len

        for idx in range(1, word_len):
            if word[idx] != word[idx-1]:
                total -= 1

        return total