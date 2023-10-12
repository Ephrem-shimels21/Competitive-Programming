# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        def findPeakIndex(mountain_arr):
            left = 0
            right = mountain_arr.length() - 1
            mid = (left + right) // 2
            while left < right:
                if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                    left = mid + 1
                    mid = (left + right) // 2
                elif mountain_arr.get(mid) > mountain_arr.get(mid + 1):
                    right = mid
                    mid = (left + right) // 2
            return mid
        peak_index = findPeakIndex(mountain_arr)
        def left_binary_search(mountain_arr):
            left = 0
            right = peak_index - 1
            if mountain_arr.get(right) == target:
                return right
            while left < right:
                mid = (left + right) // 2
                if mountain_arr.get(mid) < target:
                    left = mid + 1
                else:
                    right = mid
            if mountain_arr.get(left) == target:
                return left
            return -1
        def right_binary_search(mountain_arr):
            left = peak_index
            right = mountain_arr.length() - 1
            while left < right:
                mid = (left + right)// 2
                if mountain_arr.get(mid) > target:
                    left = mid + 1
                else:
                    right = mid
             
                    
            if mountain_arr.get(left) == target:
                return left
            return -1
        
        if left_binary_search(mountain_arr) != -1:
            return left_binary_search(mountain_arr)
        elif right_binary_search(mountain_arr) != -1:
            return right_binary_search(mountain_arr)
        return -1
        

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        