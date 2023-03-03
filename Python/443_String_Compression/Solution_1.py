class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Runtime 57 ms / Beats 86.52%
        Memory 13.9 MB / Beats 96.87%
        """
        chars_len = len(chars)
        if chars_len == 1: return 1

        left_pointer = 0
        right_pointer = 1
        res = []

        while right_pointer < chars_len:
            if chars[left_pointer] != chars[right_pointer]:
                res.append(chars[left_pointer])
                diff = right_pointer - left_pointer
                if diff != 1:
                    res.extend(list(str(diff)))
                left_pointer = right_pointer
            right_pointer += 1

        # last one
        res.append(chars[left_pointer])
        diff = right_pointer - left_pointer
        if diff != 1:
            res.extend(list(str(diff)))
        
        # change chars to res
        res_len = len(res)
        for idx in range(res_len):
            chars[idx] = res[idx]

        return res_len