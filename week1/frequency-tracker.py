class FrequencyTracker:

    def __init__(self):
        self.frequencyCount = Counter()
        self.freqs = Counter()
        
    def add(self, number: int) -> None:
        self.frequencyCount[number] += 1 #+ self.frequencyCount.get(number, 0)
        self.freqs[self.frequencyCount[number]] += 1 #+ self.freqs.get(self.frequencyCount[number], 0)
        self.freqs[self.frequencyCount[number] - 1] -= 1



    def deleteOne(self, number: int) -> None:
        if number in self.frequencyCount:
            self.frequencyCount[number] -= 1
            if  self.frequencyCount[number] == 0:
                self.frequencyCount.pop(number)
            
            self.freqs[self.frequencyCount[number]] += 1 #+ self.freqs.get(self.frequencyCount[number], 0)
            self.freqs[self.frequencyCount[number] + 1] -= 1
            
    def hasFrequency(self, frequency: int) -> bool:
        return self.freqs[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)