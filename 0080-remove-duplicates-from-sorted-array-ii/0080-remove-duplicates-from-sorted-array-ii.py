class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = {}
        k = 0
        count = len(nums)
        while k < len(nums):
                if nums[k] not in freq.keys():
                    freq[nums[k]] = 1
                    k += 1
                elif nums[k] in freq.keys():
                    freq[nums[k]] += 1
                    if freq[nums[k]] >= 3:
                        nums.remove(nums[k])
                        count -= 1 
                    else:
                        k += 1
                        
        return count
                