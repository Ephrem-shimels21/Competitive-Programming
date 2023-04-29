class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
       
        ans = []
      
        while (len(ans) < len(nums1)):
            if i >= m and j < n:
                ans.append(nums2[j])
                j +=1
            elif i < m and j >=n:
                
                ans.append(nums1[i])
                i += 1
                
            elif nums1[i] < nums2[j]:
                
                ans.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
               
                ans.append(nums2[j])             
                j += 1
                
            elif nums1[i] == nums2[j]:
                ans.append(nums1[i])
                ans.append(nums2[j])
                i += 1
                j += 1
    
        for i,ele in enumerate(ans):
            nums1[i] = ele
            
        return nums1