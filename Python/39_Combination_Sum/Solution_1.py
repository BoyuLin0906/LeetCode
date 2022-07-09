class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Runtime: 115 ms, faster than 56.66% of Python3 online submissions for Combination Sum.
        Memory Usage: 18.1 MB, less than 5.22% of Python3 online submissions for Combination Sum.
        """
        # queue
        candidates_len = len(candidates)
        results = list()
        combination_queue = list()
        
        # (combination / start_idx)
        for idx in range(candidates_len):
            combination_queue.append(([candidates[idx]], idx))
        
        combination_queue = deque(combination_queue)
        
        while combination_queue:
            combination, start_idx = combination_queue.popleft()
            
            _sum = sum(combination)
            if _sum == target: results.append(combination)
            elif _sum < target:
                for idx in range(start_idx, candidates_len):
                    combination_queue.append((combination + [candidates[idx]], idx))
        
        return results