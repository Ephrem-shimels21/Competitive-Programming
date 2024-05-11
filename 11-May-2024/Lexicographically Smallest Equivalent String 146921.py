# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            
            return parent[node]
        
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 < parent2:
                parent[parent2] = parent1
            else:
                parent[parent1] = parent2

        
        parent = [i for i in range(26)]

        for i in range(len(s1)):
            char1, char2 = ord(s1[i]) - ord("a"), ord(s2[i]) - ord("a")
            union(char1, char2)
        
        equi_string = []
        for letter in  baseStr:
            idx = ord(letter) - ord("a")
            equi_string.append(chr(find(idx) + ord("a")))
        
        return "".join(equi_string)


        
        