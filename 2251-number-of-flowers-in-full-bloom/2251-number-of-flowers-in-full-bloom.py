class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        """
        :type flowers: List[List[int]]
        :type people: List[int]
        :rtype: List[int]
        """
        # ans = []
        # for person in people:
        #     count = 0
        #     for initial,ending in flowers:
        #         if person >= initial and person <= ending:
        #             count += 1
        #     ans.append(count)
        # return ans
        sortedPeople = people[::]
        sortedPeople.sort()
        flowers.sort(key = lambda x :x[0]) 
        heap = []
        heapq.heapify(heap)
        person_flower = {}
        i = 0
        for person in sortedPeople:
            while i < len(flowers) and flowers[i][0] <= person:
                heapq.heappush(heap,flowers[i][1])
                i += 1
            while heap and heap[0] < person:
                heapq.heappop(heap)
            
            person_flower[person] = len(heap)
        
        ans = []
        for person in people:
            ans.append(person_flower[person])
        return ans
                
            
        
                
        