class Solution(object):
   def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        rearrangedList=[]
        mid=nums[len(nums)//2]
        lessHalf=nums[:len(nums)//2+1]
        print(lessHalf)
        highHalf=nums[len(nums)//2+1:]
        for i in range(len(nums)):
            if (len(lessHalf) != 0) or (len(highHalf) != 0):
                if  len(highHalf) == 0:
                    rearrangedList.append(lessHalf.pop(0))
                elif len(lessHalf) == 0:
                     rearrangedList.append(highHalf.pop(0))
                else:
                    rearrangedList.append(lessHalf.pop(0))
                    rearrangedList.append(highHalf.pop(0))
        return rearrangedList
