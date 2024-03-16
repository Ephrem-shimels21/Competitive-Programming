class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals_copy = []

        for idx, interval in enumerate(intervals):
            start, end = interval
            intervals_copy.append([start, end, idx])

        intervals_copy.sort(key = lambda x : x[0])
        output = []
        print(intervals_copy)

        for interval in intervals:
            start, end = interval
            l = 0
            r = len(intervals) - 1
            curr = float('inf')

            while l <= r:
                mid = (l + r) // 2
                startj, endj, idx = intervals_copy[mid]
                if startj > end:
                    if (curr != float('inf') and intervals[curr][0] > startj) or curr == float('inf'):
                        curr = idx
                    r = mid  - 1  
                elif startj == end:
                    curr = idx
                    break              
                else:
                    l = mid + 1
            if curr == float('inf'):
                output.append(-1)
            else:
                output.append(curr)
        
        return output