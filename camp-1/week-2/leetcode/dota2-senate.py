class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        Radiant = deque()
        Dire = deque()
        
        for index,person in enumerate(senate):
            if person == "R":
                Radiant.append(index)
            elif person == "D":
                Dire.append(index)
        
        while Radiant and Dire:
            r = Radiant.popleft()
            d = Dire.popleft()
            if r < d:
                Radiant.append(r + n)
            elif d < r:
                Dire.append(d + n)
        
        
        if Radiant:
            return "Radiant"
        else:
            return "Dire"