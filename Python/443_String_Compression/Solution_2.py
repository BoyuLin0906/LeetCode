class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Runtime 57 ms / Beats 86.52%
        Memory 13.9 MB / Beats 96.87%
        """
        chars.append(" ")
        chars_len = len(chars)
        start_pointer = 0
        compress_pointer = 0

        for idx in range(chars_len):
            if chars[start_pointer] != chars[idx]:
                # char
                chars[compress_pointer] = chars[start_pointer]
                compress_pointer += 1
                # number
                count = idx-start_pointer
                if count > 1:
                    for char in str(count):
                        chars[compress_pointer] = char
                        compress_pointer += 1
                start_pointer = idx

        return compress_pointer