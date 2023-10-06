class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {1:1}
        def dfs(num):
            if num in dp:
                return dp[num]
            dp[num] = 0 if num == n else num
        
            for i in range(num):
                product = dfs(i) * dfs(num - i)
                dp[num] = max(dp[num],product)
            return dp[num]
        
        return dfs(n)
                
        
        