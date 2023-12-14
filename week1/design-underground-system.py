class UndergroundSystem:

    def __init__(self):
        self.starting_station = {}
        self.total = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.starting_station[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startingStation, time = self.starting_station[id]
        
        if (startingStation, stationName) not in self.total:
            self.total[(startingStation, stationName)] = [t - time, 1]
        else:
            self.total[(startingStation, stationName)][0] += t - time
            self.total[(startingStation, stationName)][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.total[(startStation, endStation)] 
        
        return total / count
            
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)