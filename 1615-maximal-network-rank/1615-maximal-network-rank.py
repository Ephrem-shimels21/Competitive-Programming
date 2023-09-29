class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        cities = set()
        for road in roads:
            cities.add(road[0])
            cities.add(road[1])
        citiesL = list(cities)
        citiesL.sort()
        if len(roads) == 0:
            return 0
        city_roads = dict()
        for i in range(n):
            for road in roads:
                if i not in city_roads.keys() and i in road:
                    city_roads[i] = 1
                elif i in city_roads.keys() and i in road:
                    city_roads[i] += 1
        max_connection = [0,[]]
        
        for i in (citiesL):
            for j in citiesL:
                if i != j:
                    if city_roads[i] + city_roads[j] > max_connection[0]:
                        if [i,j] in roads or [j,i] in roads:
                            max_connection[0] = city_roads[i] + city_roads[j] - 1
                            max_connection[1] = [i,j]
                        else:
                            max_connection[0] = city_roads[i] + city_roads[j] 
                            max_connection[1] = [i,j]

       
        return max_connection[0]
                
                    
        