class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from itertools import permutations
        # Memory Limit Exceeded
        s1_permutations = [ ''.join(s1_tuple) for s1_tuple in permutations(s1) ]
        for s1_permutation in s1_permutations: 
            if s1_permutation in s2 : return True
        
        return False