class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        r = len(citations)
        if len(set(citations)) == 1 and citations[0] == 0:
            hidx = 0
        else:
            hidx = 1

        while l < r:
            mid = (l + r + 1) // 2
            if  mid <= citations[len(citations) - mid] :
                hidx = max(hidx, mid)
                l  = mid 
            else:
                r = mid - 1
        
        return hidx

        