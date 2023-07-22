class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # if x == 0:
        #     return 0
        # elif x == 1:
        #     return 1
        result = 0
        lo = 0
        hi = x
        mid = (lo + hi)  // 2
        while lo <= hi:
            if mid ** 2 > x:
                    hi = mid - 1
                    mid = (lo + hi) // 2
            elif mid ** 2 < x:
                    result = mid
                    lo = mid + 1
                    mid = (lo + hi) // 2
            elif mid ** 2 == x:
                return mid
        return result
            
        