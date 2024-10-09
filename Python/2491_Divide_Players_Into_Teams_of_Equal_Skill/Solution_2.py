"""
Runtime 384 ms / Beats 89.57%
Memory 29.57 MB / Beats 41.34%
"""
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill_len = len(skill)
        total_skill = sum(skill)
        skill_frequency = [0] * 1001

        if total_skill % (skill_len // 2) != 0:
            return -1

        for player_skill in skill:
            skill_frequency[player_skill] += 1

        target_team_skill = total_skill // (skill_len // 2)
        chemistry_sum = 0
        for player_skill in skill:
            partner_skill = target_team_skill - player_skill

            if skill_frequency[partner_skill] == 0:
                return -1

            chemistry_sum += player_skill * partner_skill
            skill_frequency[partner_skill] -= 1
        
        return chemistry_sum // 2