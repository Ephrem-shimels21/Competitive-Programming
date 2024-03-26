class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersection = []
       
        f = 0
        s = 0
        while f < len(firstList) and s < len(secondList):
            
            maxx = max(firstList[f][0], secondList[s][0])
            minn = min(firstList[f][1], secondList[s][1])
             
            if maxx <= minn:
                intersection.append([maxx, minn])
            if firstList[f][1] < secondList[s][1]:
                    f += 1
            else:
                    s += 1

        return intersection

                
                



        