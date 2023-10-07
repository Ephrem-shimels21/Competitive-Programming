class Solution(object):
    def numOfArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        cache = {}
        
        def helper(i, maxSoFar, remain):
            if i == n:
                if remain == 0:
                    return 1
                return 0
            if (i,maxSoFar, remain) in cache:
                return cache[(i, maxSoFar, remain)]
            ans = (maxSoFar * helper(i + 1, maxSoFar, remain)) % mod
            
            for j in range(maxSoFar + 1, m + 1):
                cache[(i + 1,j,remain - 1)] = helper(i + 1, j, remain - 1)
                ans = (ans + helper(i + 1,j, remain - 1)) % mod
            
            return ans
        mod = 10 ** 9 + 7
        return helper(0,0,k)
        