class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        possiblities = []
        if c > 4:
            possibilites = [x for x in range(int(c ** 0.5) + 1)]
        else:
            possibilites = [x for x in range(c + 1)]
        
        left  = 0
        right = len(possibilites) - 1
        while left <= right:
            if possibilites[left] ** 2 + possibilites[right] ** 2 == c:
                return True
            elif possibilites[left] ** 2 + possibilites[right] ** 2  < c:
                left += 1
            elif possibilites[left] ** 2 + possibilites[right] ** 2 > c:
                right -= 1
        return False
        