class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_c = Counter(nums1)

        result = []

        for num in nums2:
            if nums1_c.get(num,0):
                result.append(num)
                nums1_c[num] -= 1
        return result

       