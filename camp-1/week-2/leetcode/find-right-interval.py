class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        index_start = {}
        starts = []

        for i in range(len(intervals)):
            index_start[intervals[i][0]] = i
            starts.append(intervals[i][0])
        
        res = []
        starts.sort()
        for j in range(len(intervals)):
            idx = bisect_left(starts, intervals[j][1])

            if idx < len(intervals):
                res.append(index_start[starts[idx]])
            
            else:
                res.append(-1)
        
        return res

        