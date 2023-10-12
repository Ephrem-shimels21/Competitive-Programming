class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # for index,num in enumerate(arr):
        #     if num > arr[index + 1]:
        #         return index
        left = 0
        right = len(arr) - 1
        mid = (left + right) // 2
        
        while left < right:
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
                mid = (left + right) // 2
            elif arr[mid] > arr[mid + 1]:
                right = mid
                mid = (left + right) // 2
            # if left == right:
            #     return right
        return mid