class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_li = s1.split()
        s2_li = s2.split()
        s1_count = Counter(s1_li)
        s2_count = Counter(s2_li)
        ans = []
        for word in s1_count:
            if s1_count[word] == 1 and word not in s2_count:
                ans.append(word)
        
        for strr in s2_count:
            if s2_count[strr] == 1 and strr not in s1_count:
                ans.append(strr)
        
        return ans
        