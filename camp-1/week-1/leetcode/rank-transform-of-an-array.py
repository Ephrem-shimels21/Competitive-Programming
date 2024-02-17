class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_c = defaultdict(int)
        arr_set = list(set(arr))
        arr_set.sort()
        for i in range(len(arr_set)):
            arr_c[arr_set[i]] = i + 1 
        
      
        for idx,num in enumerate(arr):
            ix = arr_c[num]
            arr[idx]  = ix
        
        return arr
        

        