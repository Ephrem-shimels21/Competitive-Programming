# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def __init__(self):
        self.memo = defaultdict(int)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        if n not in self.memo:
            self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        
        return self.memo[n]

        