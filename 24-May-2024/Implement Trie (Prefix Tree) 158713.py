# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        curr = self
        for letter in word:
            idx = ord(letter) % 97
            if curr.children[idx] is None:
                curr.children[idx] =  Trie()
            curr = curr.children[idx]
        curr.is_end = True

    
    def search(self, word: str) -> bool:
        last_node = self.search_last_letter(word)

        return last_node is not None and last_node.is_end

        

    def startsWith(self, prefix: str) -> bool:
        last_node = self.search_last_letter(prefix)
        return last_node is not None
     
    def search_last_letter(self, word):
        curr = self

        for letter in word:
            idx = ord(letter) % 97
            if curr.children[idx] is None:
                return None
            curr = curr.children[idx]
        
        return curr
    



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)