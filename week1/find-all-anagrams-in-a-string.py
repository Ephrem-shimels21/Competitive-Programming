class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):return []
        start = 0
    
        sCount, pCount = {}, {}
        
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i],0)
            sCount[s[i]] = 1 + sCount.get(s[i],0)
        
        result = [0] if sCount == pCount else []
        
        for end in range(len(p),len(s)):
            # print(start,end,sCount,pCount)
            sCount[s[end]] = 1 + sCount.get(s[end],0)
            
            sCount[s[start]] -= 1
            
            if sCount[s[start]] == 0:
                sCount.pop(s[start])
            start += 1
            
            if sCount == pCount:
                result.append(start)
        
            

        return result
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         substrings = []
#         p_set  = set(p)
#         n = len(p)
#         substring_set = set()
        
#         while end < len(s):
#             if end - start == n:
#                 if substring_set == p_set:
#                     substrings.append(start)
#                     substring_set.remove(s[start])
#                     start += 1
#                     substring_set.add(s[end])
#                     end += 1
#                 else:
#                     substring_set.remove(s[start])
#                     start += 1
#                     end += 1
#             else:
#                 substring_set.add(s[end])
#                 end += 1
#             print(start,end,substring_set)
#         return substrings
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
 
#         letters_in_P = set(p)
#         visited = set()
        
#         while end < len(s):
#             print("at start",start,end)
#             if end - start == n:
#                 if len(visited) == len(letters_in_P):
#                     substrings.append(start)
#                     visited.remove(s[start])
#                     start += 1
#                 else:
#                     print(visited)
#                     visited.remove(s[start])
#                     start += 1
#                     end += 1
#             else:
#                 while end - start < n:
#                     if s[end] in letters_in_P:
#                         visited.add(s[end])
#                     elif s[end] not in letters_in_P:
#                         start = end + 1
#                         visited.clear()
#                     end += 1
#             print(start,end)
#         return substrings



            
            