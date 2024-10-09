"""
Runtime 405 ms / Beats 50.09%
Memory 29.32 MB / Beats 96.63%
"""

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        total_skill = skill[0] + skill[-1]
        chemistry_sum = 0

        left_idx, right_idx = 0, len(skill)-1
        while left_idx < right_idx:
            if total_skill != skill[left_idx] + skill[right_idx]:
                return -1
            
            chemistry_sum += skill[left_idx] * skill[right_idx]
            left_idx += 1
            right_idx -= 1

        return chemistry_sum