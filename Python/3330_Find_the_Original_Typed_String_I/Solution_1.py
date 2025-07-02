class Solution:
    def possibleStringCount(self, word: str) -> int:
        """
        Runtime 43 ms / Beats 31.09%
        Memory 17.84 MB / Beats 31.37%
        """
        total = 1
        prev_idx = 0
        for idx in range(1, len(word)):
            if word[idx] != word[prev_idx]:
                total += (idx - prev_idx - 1)
                prev_idx = idx
        total += (len(word) - prev_idx - 1)

        return total