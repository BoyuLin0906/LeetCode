class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        Runtime: 384 ms, faster than 82.74% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
        Memory Usage: 22.5 MB, less than 86.73% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
        """
        # Rolling Hash
        required_count = 2 ** k
        visited_list = [False] * required_count
        mask = required_count - 1 # 3: 11, 7: 111, 17: 1111
        hash_key = 0
        
        for idx in range(len(s)):
            hash_key = ((hash_key << 1) & mask) | int(s[idx])
            if idx >= k-1 and not visited_list[hash_key]:
                visited_list[hash_key] = True
                required_count -= 1
                if not required_count: return True
                
        return False