class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        limit = len(nums) // 3
        ans = set()
        
        for index,num in enumerate(nums):
            if nums.count(num) > limit:
                if num not in ans:
                    ans.add(num)
                else:
                    continue
           
        return list(ans)