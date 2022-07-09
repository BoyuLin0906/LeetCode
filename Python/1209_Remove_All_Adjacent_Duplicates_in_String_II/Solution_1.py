class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        Runtime: 1281 ms, faster than 5.01% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
        Memory Usage: 15.4 MB, less than 93.07% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
        """
        idx = 0
        prev_char = ''
        prev_char_idx = 0
        counts_dict = defaultdict(list)
        count = 1
        
        while idx < len(s):
            char = s[idx]
            if prev_char == s[idx]:
                count += 1
                if count >= k:
                    s = s[:idx-(k-1)] + s[idx+1:]
                    count = 1
                    idx -= k
                    if idx < 0: idx = 0
                    if s and counts_dict[s[idx]]:
                        idx -= (counts_dict[s[idx]].pop() - 1)   
            else:
                counts_dict[prev_char].append(count)
                count = 1
            if s:
                prev_char = s[idx]
                idx += 1
            
        return s
            