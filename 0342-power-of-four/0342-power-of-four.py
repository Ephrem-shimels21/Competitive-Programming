class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
    
     
        if n == 1:
            return True
        if n < 4:
            return False
        
        return n % 4 == 0 and self.isPowerOfFour(n // 4)

      
        