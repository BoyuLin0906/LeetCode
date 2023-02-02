class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        Runtime 35 ms / Beats 87.31%
        Memory 13.9 MB / Beats 77.66%
        """
        if len(words) == 1: return True

        order_table = dict()
        for index, alphabet in enumerate(order):
            order_table[alphabet] = index

        for idx in range(len(words)-1):
            word_curr, word_next = words[idx], words[idx+1]
            is_order = False
            word_len = min(len(word_curr), len(word_next))

            for alp_idx in range(word_len):
                # smaller
                if order_table[word_curr[alp_idx]] < order_table[word_next[alp_idx]]:
                    is_order = True
                    break
                # bigger, fail
                elif order_table[word_curr[alp_idx]] > order_table[word_next[alp_idx]]: 
                    return False
            
            # alphabets are same, compare length
            if not is_order and len(word_curr) > len(word_next):
                return False
            
        return True