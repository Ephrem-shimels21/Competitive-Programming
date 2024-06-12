# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        occurence = 0
        nums2 = nums[::]

        for idx in range(len(nums) - 1):
            if nums[idx] > nums[idx + 1]:
                if nums[idx + 1] == nums[idx - 1]:
                    nums[idx] = nums[idx + 1]
                else:
                    nums[idx] = nums[idx + 1] - 1

                if idx + 2 < len(nums) and nums2[idx] == nums2[idx + 2]:
                    nums2[idx + 1] = nums2[idx]
                else:
                    nums2[idx + 1] = nums2[idx] + 1
                break
        temp1 = nums[::]
        temp2 = nums2[::]
        nums.sort()
        nums2.sort()
        
        if nums == temp1 or nums2 == temp2:
            return True
        return False

        