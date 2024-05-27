# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Trie:
    def __init__(self):
        self.children  = [None] * 26
        self.is_end = False
    
    def insert(self, word):
        root = self
        for letter in word:
            idx = ord(letter) - 97

            if root.children[idx] == None:
                root.children[idx] = Trie()
            
            root = root.children[idx]
        
        root.is_end = True
    
    def longest_word(self):
        def dfs(node, path):
            nonlocal longest
            if not node.is_end and path != "":
                return 
            
            if len(path) > len(longest):
                longest = path
            
            for i in range(26):
                if node.children[i]:
                    letter = chr(i + 97)
                    dfs(node.children[i], path + letter)
        
        longest = ""
        dfs(self, "")
        return longest
            

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        return trie.longest_word()

        