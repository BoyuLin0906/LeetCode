"""
Runtime 36 ms / Beats 50.31%
Memory 16.62 MB / Beats 13.04%
"""

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split(" ")
        words2 = sentence2.split(" ")

        if len(words1) < len(words2):
            words1, words2 = words2, words1

        start_idx = 0
        words1_end_idx = len(words1)-1
        words2_end_idx =  len(words2)-1

        while start_idx < len(words2) and words1[start_idx] == words2[start_idx]:
            start_idx += 1

        while words2_end_idx >= 0 and words1[words1_end_idx] == words2[words2_end_idx]:
            words1_end_idx -= 1
            words2_end_idx -= 1

        return words2_end_idx < start_idx