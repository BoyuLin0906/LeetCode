class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
        Runtime: 532 ms, faster than 80.22% of Python3 online submissions for Maximum Product of Word Lengths.
        Memory Usage: 14.5 MB, less than 42.09% of Python3 online submissions for Maximum Product of Word Lengths.
        """
        # Bit Mask
        words_len = len(words)
        bit_mask, lengths = [0] * words_len, [0] * words_len
        
        for i in range(words_len):
            # abc -> a:1, b:2 , c:3 -> bits: 111
            for char in words[i]: bit_mask[i] = bit_mask[i] | 1 << (ord(char) - 97)
            lengths[i] = len(words[i])
                
        _max = 0
        for i in range(words_len):
            for j in range(i+1, words_len):
                # abc & a -> 111 & 1 = 1
                # abc & d -> 111 & 1000 = 0
                if not bit_mask[i] & bit_mask[j]:
                    _max = max( _max, lengths[i] * lengths[j])
                    
        return _max