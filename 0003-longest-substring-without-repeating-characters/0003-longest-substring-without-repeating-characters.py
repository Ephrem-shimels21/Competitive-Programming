class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      a = 0
      b = 0
      c = {}
      sol = 0
      while b < len(s):
         if s[b] not in c or a>c[s[b]]:
            sol = max(sol,(b-a+1))
            c[s[b]] = b
         else:
            a = c[s[b]]+1
            sol = max(sol,(b-a+1))
            b-=1
         b+=1
      return sol
        