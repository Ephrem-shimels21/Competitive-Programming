class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_counter = Counter(nums)

        ans = []
        for num in range(1,len(nums) + 1):
            if num not in nums_counter:
                ans.append(num)
        
        return ans
        