class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        if n == 1:
            return True
        while True:
            temp = 0
            while n:
                digit = n % 10
                temp += digit ** 2
                n = n // 10
            if temp in visited:
                return False
            if temp == 1:
                return True
            visited.add(temp)
            n = temp

                
        