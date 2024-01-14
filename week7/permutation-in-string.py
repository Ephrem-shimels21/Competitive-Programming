class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count,s2Count = {}, {}
        
        for i in range(len(s1)):
            s1Count[s1[i]] = 1 + s1Count.get(s1[i],0)
            s2Count[s2[i]] = 1 + s2Count.get(s2[i],0)
        
        if s1Count == s2Count:
            return True
        start = 0
        
        for end in range(len(s1),len(s2)):
            
            s2Count[s2[end]] = 1 + s2Count.get(s2[end],0)
            
            s2Count[s2[start]] -= 1
            if s2Count[s2[start]] == 0:
                s2Count.pop(s2[start])
            start += 1
            
            if s1Count == s2Count:
                return True
        return False
        