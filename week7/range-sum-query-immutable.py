class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        prefixs = []
     
        for index,num in enumerate(self.nums):
            if index == 0:
                prefixs.append(num)
            else:
                prefixs.append(num + prefixs[index - 1])
        summ = prefixs[right] - prefixs[left] + self.nums[left]
        return summ
                
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)