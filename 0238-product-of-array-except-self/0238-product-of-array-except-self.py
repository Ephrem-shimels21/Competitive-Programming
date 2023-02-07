class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] 
        for n in nums[:-1]:
            prefix.append(prefix[-1] * n)
        suffix = [1]  # last element's suffix
        for i in range(len(nums)-1):
            suffix.append(suffix[-1] * nums[~i])
        print(suffix)  # [1, 4, 12, 24]
        output = []
        for i in range(len(prefix)):
            output.append(prefix[i] * suffix[~i])
        return output
