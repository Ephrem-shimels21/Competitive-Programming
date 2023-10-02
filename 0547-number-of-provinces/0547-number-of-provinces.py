class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def dfs(start):
            visited.add(start)
            
            for ending in range(len(isConnected)):
                if isConnected[start][ending] and ending not in visited:
                    dfs(ending)
        
        
        no_provinces = 0
        
        visited = set()
        
        for starting in range(len(isConnected)):
            if starting not in visited:
                no_provinces += 1
                dfs(starting)
                
        return no_provinces