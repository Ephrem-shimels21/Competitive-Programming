class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        limit = len(nums) // 3
        ans = []
        
        for index,num in enumerate(nums):
            if nums.count(num) > limit:
                if num not in ans:
                    ans.append(num)
                else:
                    continue
           
        return ans