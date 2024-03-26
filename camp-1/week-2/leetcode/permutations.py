class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutaions = []
        def miniPermute(path, visited):
            if len(path) == len(nums):
                permutaions.append(path[:])
                return 
            
            for j in range(0, len(nums)):
                if nums[j] not in visited:
                    path.append(nums[j])
                    visited.add(nums[j])
                    miniPermute(path, visited)
                    visited.remove(nums[j])
                    path.pop()

        miniPermute([], set())
        return permutaions
            
        