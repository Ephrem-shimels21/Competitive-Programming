class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stat = {}
        for i in range(len(nums2)):
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    stat[nums2[i]] = nums2[j]
                    break
            if nums2[i] not in stat:
                stat[nums2[i]] = -1
        result = [stat[x] for x in nums1]
        return result