class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_d = {}
        for i, letter in enumerate(order):
            order_d[letter] = i
        
        for i in range(len(words) - 1):
               for j in range(len(words[i])):
                   if j >= len(words[i + 1]):
                       return False
                   if words[i][j] != words[i + 1][j]:
                       if order_d[words[i][j]] > order_d[words[i + 1][j]]:
                           return False
                       break
        return True 

        