class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merged = ""
        
        while word1  and word2:
            if word1[0] > word2[0]:
                merged += word1[0]
                word1 = word1[1:]
            
            elif word2[0] > word1[0]:
                merged +=  word2[0]
                word2 = word2[1:]
            
            else:
                i = 0
                
                while i < len(word1) and i < len(word2) and word1[i] == word2[i]:
                    i += 1
                
                if i < len(word1) and i < len(word2):
                    
                    if word1[i] < word2[i]:
                        merged += word2[0]
                        word2 = word2[1:]
                    elif word2[i] < word1[i]:
                        merged += word1[0]
                        word1 = word1[1:]
                else:
                    
                    if len(word1) <= len(word2):
                        merged += word2[0]
                        word2 = word2[1:]
                    elif len(word2) < len(word1):
                        merged += word1[0]
                        word1 = word1[1:]
        
        if word1:
            merged += word1
        else:
            merged += word2
        
       
        return merged
        