class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left_p = []
        p = []
        right_p = []

        for num in nums:
            if num < pivot:
                left_p.append(num)
            elif num == pivot:
                p.append(num)
            elif num > pivot:
                right_p.append(num)
        return left_p + p + right_p