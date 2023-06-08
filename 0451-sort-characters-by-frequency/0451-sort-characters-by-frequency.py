class Solution:
    def frequencySort(self, s: str) -> str:
        list_s = list(s)
        freq = {}
        result = ""

        for letter in list_s:
            if letter not in freq.keys():
                freq[letter] = 1
            else:
                freq[letter] += 1
                
    
        frequencies = list(freq.values())
        frequencies.sort()
        frequencies.reverse()
   
        
        for value in frequencies:
            for letter in freq.keys():
                if freq[letter] == value and  letter not in result:
                    for i in range(value):
                        result += letter
        return result
            
        