class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_size = 1
        left, right = 0, 1
        previous_comparison = ""
        
        while right < len(arr):
            
            if arr[right] > arr[right - 1] and previous_comparison != ">":
                max_size = max(max_size, right - left + 1)
                previous_comparison = ">"
                right += 1
            elif arr[right] < arr[right - 1] and previous_comparison != "<":
                max_size = max(max_size, right - left + 1)
                previous_comparison = "<"
                right += 1
            else:
                right = right + 1 if arr[right] == arr[right - 1] else right
                
                left = right - 1
                previous_comparison = ""
        return max_size

       