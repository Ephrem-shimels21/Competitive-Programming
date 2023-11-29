class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float("inf")

        for string in strs:
            min_length = min(min_length, len(string))
        
        ans = ""
        for i in range(min_length):
            charr = set()
            for string in strs:
               charr.add(string[i])
            
            if len(charr) == 1:
                ans += strs[0][i]
                charr.clear()
            else:
                if ans:
                    return ans
                return ""
        return ans