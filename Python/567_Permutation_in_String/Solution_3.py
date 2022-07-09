class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        
        s1_len, s2_len = len(s1), len(s2)
        s1_counter, s2_counter = Counter(s1), Counter(s2[:s1_len])
        
        for i in range(s2_len-s1_len+1):
            if s2_counter == s1_counter: return True
            # optimize
            if i + s1_len < s2_len:
                s2_counter[s2[i]] -= 1
                s2_counter[s2[i + s1_len]] += 1
            
        return False