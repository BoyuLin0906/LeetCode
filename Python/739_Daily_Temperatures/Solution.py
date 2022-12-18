class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for idx, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                _, popped_idx = stack.pop()
                res[popped_idx] = idx - popped_idx
            stack.append((temperature, idx))
        
        return res