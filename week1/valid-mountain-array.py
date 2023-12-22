class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        
        mountain = False

        for i in range(len(arr) - 1):
            if mountain and arr[i] <= arr[i + 1]:
                return False
            elif arr[i] == arr[i + 1]:
                return False
            elif arr[i] > arr[i + 1]:
                mountain = True
            if i == 0 and mountain:
                return False
        if not mountain:
            return False
        return True
        