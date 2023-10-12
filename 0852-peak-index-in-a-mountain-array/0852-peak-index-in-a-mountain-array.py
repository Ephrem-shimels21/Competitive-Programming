class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        for index,num in enumerate(arr):
            if num > arr[index + 1]:
                return index