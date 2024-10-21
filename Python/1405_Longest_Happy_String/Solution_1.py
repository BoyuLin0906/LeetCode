"""
Runtime 21 ms / Beats 99.89%
Memory 16.81 MB / Beats 29.54%
"""

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        priority_queue = []
        if a > 0:
            heapq.heappush(priority_queue, (-a, "a"))
        if b > 0:
            heapq.heappush(priority_queue, (-b, "b"))
        if c > 0:
            heapq.heappush(priority_queue, (-c, "c"))
        
        output = []
        while priority_queue:
            count, char = heapq.heappop(priority_queue)
            count = -count
            if len(output) >= 2 and output[-1] == char and output[-2] == char:
                if not priority_queue:
                    break
                
                second_count, second_char = heapq.heappop(priority_queue)
                second_count = -second_count
                output.append(second_char)

                if second_count - 1 > 0:
                    heapq.heappush(priority_queue, (-(second_count - 1), second_char))

                heapq.heappush(priority_queue, (-count, char))
            else:
                count -= 1
                output.append(char)
                if count > 0:
                    heapq.heappush(priority_queue, (-count, char))

            
        return "".join(output)