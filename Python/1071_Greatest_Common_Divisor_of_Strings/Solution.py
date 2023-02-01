class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Runtime 27 ms / Beats 95.70%
		Memory 14 MB / Beats 23.70%
        """
        if (str2 + str1) != (str1 + str2) : 
            return ""
        
        idx = math.gcd(len(str1), len(str2))
        return str2[:idx]