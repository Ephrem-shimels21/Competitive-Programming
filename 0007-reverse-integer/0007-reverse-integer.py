class Solution:
    def reverse(self, x: int) -> int:
        reverted = ''
        if x < 0:
            normal = str(-(x))
        else:
            normal = str(x)
        
        while normal:
            rem = int(normal) % 10
            reverted += str(rem)
            normal = normal[:len(normal) - 1]
            
           
        if x < 0:
            reverted = -1 * int(reverted)
            
        if int(reverted) > (2 ** 31 - 1)  or int(reverted) < - (2 ** 31):
            return 0
        return int(reverted)
        