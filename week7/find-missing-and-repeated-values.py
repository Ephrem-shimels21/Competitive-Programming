class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        element_count = defaultdict(int)
        n = len(grid)

        for i in range(n):
            for j in grid[i]:
                element_count[j] += 1
        
        ans = []
        b = 0
        for num in range(1, n ** 2  + 1):
            if num not in element_count:
                b = num
            
            if element_count[num] == 2:
                ans.append(num)
        
        ans.append(b)

        return ans


        