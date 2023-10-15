class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        start = 0
        end = len(skill) - 1
        
        no_teams = len(skill) // 2
        skill_sum_in_team = sum(skill) // no_teams
        
        skill.sort()
        
        count = 0
        ans = 0
        while start <= end:
            if skill[start] + skill[end] == skill_sum_in_team:
                count += 1
                ans += skill[start] * skill[end]
            else:
                return  -1
            start += 1
            end -= 1
        if no_teams != count:
            return -1
        return ans
                
            
        
        