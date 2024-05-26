# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.idx = -1
    
    def insert(self, word, idx):
        root = self

        for letter in word:
            indx = ord(letter) - 97

            if root.children[indx] is None:
                root.children[indx] = Trie()
            
            root = root.children[indx]
        root.idx = idx
    
    def search(self, word):
        root = self

        for letter in word:
            lett_idx = ord(letter) - 97

            if root.children[lett_idx] == None:
                return -1
            
            root = root.children[lett_idx]
        
            if root.idx != -1:
                return root.idx

        return -1
    


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()

        for idx, word in enumerate(dictionary):
            trie.insert(word, idx)
        
        new_sentence = []

        for word in sentence.split():
            indx = trie.search(word)

            new_sentence.append(dictionary[indx] if indx != -1 else word) 


        return " ".join(new_sentence) 
       