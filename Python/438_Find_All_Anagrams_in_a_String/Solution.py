class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Runtime 121 ms / Beats 76.58%
        Memory 15.2 MB / Beats 74.41%
        """
        p_len = len(p)
        s_len = len(s)
        if p_len > s_len: return []

        def check():
            is_ok = True
            for key, val in p_amount.items():
                if p_dict[key] != val:
                    is_ok = False
                    break
            return is_ok

        p_dict = collections.defaultdict(int)
        p_amount = collections.defaultdict(int)

        for char in p: 
            p_amount[char] += 1

        res = list()
        for idx in range(p_len):
            p_dict[s[idx]] += 1
        if check(): res.append(0)

        for idx in range(1, s_len-p_len+1):
            p_dict[s[idx-1]] -= 1
            p_dict[s[idx+p_len-1]] += 1
            if check(): res.append(idx)

        return res
