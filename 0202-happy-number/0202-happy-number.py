class Solution:
    def __init__(self):
        self.visited = set()
    def isHappy(self, n: int) -> bool:
        num = n
        if num == 1:
            return True
        elif num in self.visited:
            return False
        else:
            self.visited.add(num)
            temp = 0
            while  num:
                digit = num % 10
                temp += digit ** 2
                num = num // 10
            return self.isHappy(temp)
            
            
        