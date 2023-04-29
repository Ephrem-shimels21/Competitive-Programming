class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i,x in enumerate(nums):
            store[i] = (x,i)
           
        original = nums[::]
        nums.sort()
        i = 0
        j = len(nums) - 1       
        while True:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] == target:
                ans = []
                for ele in store.values():
                    if nums[i] == ele[0] or nums[j] == ele[0]:
                        ans.append(ele[1])
                return ans
        