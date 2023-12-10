class Solution:
    def printVertically(self, s: str) -> List[str]:
        sl = s.split()
        maxL = 0

        for word in sl:
            maxL = max(maxL, len(word))
        ans = []
        for i in range(maxL):
            temp = ""
            for word in sl:
                if i < len(word):
                    temp += word[i]
                else:
                    temp += " "
            ans.append(temp.rstrip())
        return ans

        
        