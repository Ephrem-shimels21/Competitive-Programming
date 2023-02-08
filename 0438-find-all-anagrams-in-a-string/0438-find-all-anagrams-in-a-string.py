class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:    
        ns, np = len(s), len(p)
        if np > ns:
            return []
        shash, phash = [0] * 123, [0] * 123
        res = []
        for ch in p:
            phash[ord(ch)] += 1
        for i in range(np-1):
            shash[ord(s[i])] += 1
        for i in range(np-1, ns):
            shash[ord(s[i])] += 1
            if i - np >= 0:
                shash[ord(s[i - np])] -= 1
            if shash == phash:
                res.append(i - np + 1)
        return res