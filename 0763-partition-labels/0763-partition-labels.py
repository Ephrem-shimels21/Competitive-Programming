class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        lastOccurence = {}
        
        for index,letter in enumerate(s):
            lastOccurence[letter] = index + 1
        
        size = 1
        last_occurence = lastOccurence[s[0]]
        ans = []
        # print(lastOccurence)
        
        for letter in s:
            # print(size,letter,last_occurence,lastOccurence[letter])
            last_occurence = max(last_occurence,lastOccurence[letter])
            if ans:
                if size == abs(last_occurence - sum(ans)):
                    ans.append(size)
                    size = 1
                else:
                    size += 1
                    last_occurence = max(last_occurence,lastOccurence[letter])
            else:
                if size == (last_occurence):
                    ans.append(size)
                    size = 1
                else:
                    size += 1
                    last_occurence = max(last_occurence,lastOccurence[letter])
        return ans
                    
                
            
            
        