class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([]) 
        result = []
        
        for idx, num in enumerate(nums):
            # monotonic rule
            while queue and queue[-1][0] < num:
                queue.pop()
                
            # check expired elementk       
            if queue and queue[0][1] <= idx-k:
                queue.popleft()
            
            queue.append((num, idx))
            if queue: result.append(queue[0][0])
        
        return result[k-1:]