class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        window = len(needle)
        i = 0
        
        while (i + window) <= len(haystack):
            print(haystack[i:i + window])
            if haystack[i: i + window] == needle:
                return i
            else:
                i += 1
        return -1
        
        
#         sub_haystack = ''
#         for index,letter in enumerate(haystack):
#             if len(needle) == 1:
#                 return index
            
#             if haystack[index] == needle[0] and haystack[index + 1] == needle[1]:
#                 sub_haystack = haystack[index:len(needle)]
        
#         for index,letter in enumerate(sub_haystack):
#             if letter !=
                
            
        
        