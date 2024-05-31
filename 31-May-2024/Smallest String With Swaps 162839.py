# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def find_root(x: int) -> int:
            if parent[x] != x:
                parent[x] = find_root(parent[x])
            return parent[x]

        n = len(s)
        parent = list(range(n))

        for a, b in pairs:
            parent[find_root(a)] = find_root(b)

        char_group = defaultdict(list)
    
        for i, c in enumerate(s):
            char_group[find_root(i)].append(c)
    
        for chars in char_group.values():
            chars.sort(reverse=True)
    
        output = "".join(char_group[find_root(i)].pop() for i in range(n))
    
        return output
        