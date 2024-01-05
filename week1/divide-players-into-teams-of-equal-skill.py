class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        team = len(skill) // 2
        total = sum(skill)

        if (total / team) !=  total // team:
            return -1
        
        skill.sort()

        product_sum = 0

        l = 0
        r = len(skill) - 1

        while l <= r:
            if skill[l] + skill[r] != (total // team):
                return -1
            product = skill[l] * skill[r]
            product_sum += product
            l += 1
            r -= 1
        return product_sum
        