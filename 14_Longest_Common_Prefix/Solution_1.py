class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]

        first_str, length = strs[0], 1  
        for _index in range(len(first_str)):
            for string in strs:
                if first_str != string:
                    if first_str[:length] != string[:length]:
                        return first_str[:length-1]
            length += 1
        return first_str[:length-1]