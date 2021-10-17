class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        LpsTable = self.LpsTable(needle)
        index, needle_index = 0, 0
        haystack_len = len(haystack)
        needle_len = len(needle)
        
        while(index < haystack_len and needle_index < needle_len):
            # needle_index is -1
            # char is same between haystack with index and needle with needle_index
            if needle_index == -1 or haystack[index] == needle[needle_index]:
                index += 1
                needle_index += 1
            else:
                needle_index = LpsTable[needle_index]
                
        if needle_index == needle_len:
            return index - needle_index
        else:
            return -1
        
        
    def LpsTable(self, pattern):
        # [-1, 0, 0, ... ]
        lps_list = [-1] + [0] * len(pattern)
        index, prefix_index = 1, 0
        
        while index < len(pattern):
            # prefix index + 1
            # index + 1
            # [-1, 0, 1, 2, ... ]
            if prefix_index == -1 or pattern[prefix_index] == pattern[index]:
                prefix_index += 1
                index += 1
                lps_list[index] = prefix_index
            # reset prefix index
            else:
                prefix_index = lps_list[prefix_index]
        return lps_list
        