class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
		Runtime: 2086 ms, faster than 94.88% of Python3 online submissions for Ones and Zeroes.
		Memory Usage: 307.4 MB, less than 5.12% of Python3 online submissions for Ones and Zeroes.
        """
        # Knapsack Problem
        # Recursion with @cache
        # without @cache O(n^2)
        str_counts = [(str.count('0'), str.count('1')) for str in strs]
        strs_len = len(strs)
        
        @cache
        def RecursiveFind(idx, zero_len, one_len):
            if zero_len < 0 or one_len < 0: return -inf
            elif idx == strs_len: return 0
            
            return max(RecursiveFind(idx+1, zero_len, one_len), 
                       RecursiveFind(idx+1, zero_len-str_counts[idx][0], one_len-str_counts[idx][1]) + 1)
        
        return RecursiveFind(0, m, n)