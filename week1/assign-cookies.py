class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gp = 0 
        sp = 0
        count  = 0

        while gp < len(g) and sp < len(s):
            if g[gp] <= s[sp]:
                count += 1
                gp += 1
                sp += 1
            else:
                sp += 1
        return count