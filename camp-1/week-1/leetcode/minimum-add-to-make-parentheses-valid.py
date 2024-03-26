class Solution:
    def minAddToMakeValid(self, s: str) -> int:
      
        openP = 0
        closeP = 0

        for pareth in s:
            if pareth == "(" :
                openP += 1
            elif pareth == ")" and  openP:
                openP -= 1
            else:
                closeP += 1
        
        return openP + closeP

