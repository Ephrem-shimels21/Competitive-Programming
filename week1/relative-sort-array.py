class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        idx = 0
        i = 0
        while idx < len(arr2):
            for j in range(len(arr1)):
               if arr1[j] == arr2[idx]:
                   arr1[i], arr1[j] = arr1[j], arr1[i]
                   i += 1
            idx += 1

        return arr1[:i] + sorted(arr1[i:])

        