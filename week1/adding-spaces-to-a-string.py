class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        spaces_set = {space for space in spaces}
        if 0 in spaces_set:
            ans.append(" ")
        
        for i in range(len(s)):
            if i + 1 in spaces_set:
                ans.append(s[i])
                ans.append(" ")
            else:
                ans.append(s[i])
        return "".join(ans)
        