class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # queue
        max_length = 0
        queue = deque([])
        pointer = 0
        str_len = len(s)
        
        while pointer < str_len:
            if s[pointer] in queue:
                queue.popleft()
            else:
                queue.append(s[pointer])
                pointer += 1
                max_length = max(len(queue), max_length)
            
        return max_length