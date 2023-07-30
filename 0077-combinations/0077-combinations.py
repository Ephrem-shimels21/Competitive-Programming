class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        numbers = [num for num in range(1,n + 1 )]
        print(numbers)
        combinations = []
        def backTrack(index,combination):
            if len(combination) == k:
                combinations.append(combination[:])
                return
            if index >= n:
                return
            
            combination.append(numbers[index])
            backTrack(index + 1, combination)
            combination.pop()
            
            backTrack(index + 1,combination )
        
        backTrack(0,[])
        return combinations
            
        
             
            
            
            
            
            
            
        