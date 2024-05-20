# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[] for _ in range(n + 1)]
        dp[0] = [[]]  
        
        for i in range(1, n + 1):
            for j in range(i):
                substring = s[j:i]
                if substring == substring[::-1]:  
                    for partition in dp[j]:
                        dp[i].append(partition + [substring])
        
        return dp[n]

            