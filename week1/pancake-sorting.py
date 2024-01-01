class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        p = len(arr) - 1
        k = 0
        max_num = float('-inf')
        while p >= 0:
            for idx, num in enumerate(arr[:p+1]):
                if num > max_num:
                    max_num = num
                    k = idx
            arr = arr[:k + 1][::-1] + arr[k + 1:]
            arr = arr[:p + 1][::-1] + arr[p + 1:]
            ans.append(k + 1)
            ans.append(p + 1)
            max_num = float('-inf')
            p -= 1
            
        return ans

        