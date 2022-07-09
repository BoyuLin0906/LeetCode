class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        # sort the string
        strs.sort()
        limit_len, count = len(strs[0]), 0
        # compare
        while(count < limit_len and strs[0][count] == strs[-1][count]):
            count+=1 
        return strs[0][:count]