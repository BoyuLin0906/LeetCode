class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
    	"""
    	Runtime 939 ms / Beats 99.21%
		Memory 28.4 MB / Beats 56.45%
    	"""
        counter = Counter(tasks)
        total_rounds = 0

        for count in counter.values():
            if count == 1: return -1
            total_rounds += count // 3
            total_rounds += 1 if count % 3 != 0 else 0
        return total_rounds