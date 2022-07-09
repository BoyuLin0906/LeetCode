class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Runtime: 61 ms, faster than 96.09% of Python3 online submissions for Combination Sum.
        Memory Usage: 14.1 MB, less than 21.05% of Python3 online submissions for Combination Sum.
        """
        # backtracking
        candidates_len = len(candidates)
        results = list()
        combination_queue = list()
        candidates.sort()
        
        def do_combination(combination, start_idx):
            _sum = sum(combination)
            if _sum == target: 
                results.append(combination)
                
            if _sum >= target: 
                return True
            elif _sum < target:
                for idx in range(start_idx, candidates_len):
                    if(do_combination(combination + [candidates[idx]], idx)):
                        break
                return None
            
        for idx in range(candidates_len):
            do_combination([candidates[idx]], idx)
        
        return results