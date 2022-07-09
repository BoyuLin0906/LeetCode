class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        
        s1_len, s2_len = len(s1), len(s2)
        s1_counter = Counter(s1)
        
        for i in range(s2_len-s1_len+1):
            if Counter(s2[i:s1_len+i]) == s1_counter: return True
            
        return False