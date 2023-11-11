class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        gs = 0
        ss = 0
        
        while gs < len(g) and ss < len(s):
            if g[gs] <= s[ss]:
                count += 1
                gs += 1
                ss += 1
            else:
                ss += 1
        return count
                