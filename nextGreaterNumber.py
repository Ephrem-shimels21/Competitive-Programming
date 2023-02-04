class Solution:
    def nextGreaterElement(self, nums1, nums2): 
        result=[0]*len(nums1)
        for i in range(len(nums2)-1):
            if (nums2[i] in nums1) and nums2[i] < nums2[i+1]:
                result[nums1.index(nums2[i])] = nums2[i+1]
                print(nums2[i])
            elif (nums2[i] not in nums1):
                continue
            elif (nums2[i+1] < nums2[i]):
                result[nums1.index(nums2[i])] = -1
        if(nums2[-1] in nums1):
                 result[nums1.index(nums2[-1])] = -1
            
        return result
    
ob = Solution()
print(ob.nextGreaterElement([4,1,2],[1,3,4,2]))
a ="()"
print(a.index(")"))
print(a[-1])