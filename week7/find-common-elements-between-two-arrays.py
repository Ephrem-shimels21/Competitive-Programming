class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counter = Counter(nums1)
        nums2_counter = Counter(nums2)

        ans = []
        count_1 = 0
        count_2 = 0
        for num in nums1_counter:
            if num in nums2_counter:
                count_1 += nums1_counter[num]
        ans.append(count_1)

        for num in nums2_counter:
            if num in nums1_counter:
                count_2 += nums2_counter[num]
        ans.append(count_2)

        return ans
