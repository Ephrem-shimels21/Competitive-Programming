class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        if len(nums1) <= len(nums2):
            for ele in nums1:
                if ele in nums2:
                    ans.append(ele)
                    nums2.remove(ele)
        elif len(nums2) < len(nums1):
            for ele in nums2:
                if ele in nums1:
                    ans.append(ele)
                    nums1.remove(ele)
        return ans
        