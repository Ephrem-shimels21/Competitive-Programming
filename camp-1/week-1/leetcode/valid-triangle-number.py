class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            k = i + 2
            j = i + 1
            while j < len(nums) - 1 and nums[i] != 0:
                while nums[i] != 0 and k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                count += k - j - 1
                j += 1
        return count
            
            