class DataStream:

    def __init__(self, value: int, k: int):
        self.DataStream = []
        self.value = value
        self.k = k
        self.no_value = 0
        

    def consec(self, num: int) -> bool:
        self.DataStream.append(num)
        
        if num == self.value:
            self.no_value += 1
        else:
            self.no_value = 0
      
      
        if self.no_value >= self.k:
            return True
        return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)