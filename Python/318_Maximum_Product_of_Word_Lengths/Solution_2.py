class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
        Runtime: 1506 ms, faster than 45.10% of Python3 online submissions for Maximum Product of Word Lengths.
        Memory Usage: 15.8 MB, less than 21.04% of Python3 online submissions for Maximum Product of Word Lengths.
        """
        # Set Operation 
        words_len = len(words)
        char_set = [set(words[i]) for i in range(words_len)]
        # ["a","ab","abc","d","cd","bcd","abcd"] -> [{'a'}, {'a', 'b'} ...]
        _max = 0
        for i in range(words_len):
            for j in range(i+1, words_len):
                if not char_set[i] & char_set[j]:
                    _max = max( _max, len(words[i]) * len(words[j]))
                    
        return _max