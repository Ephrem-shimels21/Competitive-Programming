# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            idx = ord(letter) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
                
            curr = curr.children[idx]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(idx, node):
            for i in range(idx, len(word)):
                char = word[i]
                if char == '.':
                    for child in node.children:
                        if child is not None and dfs(i + 1, child):
                            return True
                    return False
                else:
                    indx = ord(char) - ord('a')
                    if node.children[indx] is None:
                        return False
                    node = node.children[indx]
            return node.is_end

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord("word")
# param_2 = obj.search("word")
