class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
        Runtime: 4687 ms, faster than 17.26% of Python3 online submissions for Maximum Product of Word Lengths.
        Memory Usage: 14.5 MB, less than 42.09% of Python3 online submissions for Maximum Product of Word Lengths.
        """
        # Force
        words_len = len(words)
        _max = 0
        
        for i in range(words_len):
            for j in range(i+1, words_len):
                flag = True
                for char in words[i]:
                    if char in words[j]:
                        flag = False
                        continue
                if flag: _max = max(_max, len(words[i]) * len(words[j]))
        return _max