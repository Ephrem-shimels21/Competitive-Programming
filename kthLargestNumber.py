class Solution(object):
   def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        IntNums=list(map(int,nums))
        IntNums.sort()
        print(IntNums)
        return str(IntNums[len(nums)-k])

