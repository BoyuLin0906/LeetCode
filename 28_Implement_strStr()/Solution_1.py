class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and not needle: return 0
        # similar Rabin Karp
        needle_len = len(needle)
        for index in range(0, len(haystack)-needle_len+1):
            if haystack[index: index + needle_len] == needle:
                return index
        return -1