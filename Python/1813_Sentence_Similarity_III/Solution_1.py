"""
Runtime 33 ms / Beats 71.43%
Memory 16.70 MB / Beats 13.04%
"""

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split(" ")
        words2 = sentence2.split(" ")

        while words1 and words2 and words1[0] == words2[0]:
            words1.pop(0)
            words2.pop(0)

        while words1 and words2 and words1[-1] == words2[-1]:
            words1.pop(-1)
            words2.pop(-1)

        return not words1 or not words2