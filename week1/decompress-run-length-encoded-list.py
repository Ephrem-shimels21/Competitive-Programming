class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        
        slow, fast = 0, 1
        
        while fast < len(nums):
            while nums[slow]:
                output.append(nums[fast])
                nums[slow] -= 1
            slow += 2
            fast += 2
        return output
        