class DataStream:

    def __init__(self, value: int, k: int):
        self.DataStream = []
        self.value = value
        self.k = k
        self.length = 0
        self.previous = None
        self.no_value = None
        

    def consec(self, num: int) -> bool:
        self.DataStream.append(num)
        self.length += 1
        # index  = self.length - self.k
        # self.previous = num
        if self.previous == None:
            self.previous = num
            self.no_value = 1
        elif self.previous == num:
            self.no_value += 1
        elif self.previous != num:
            self.no_value = 1
            self.previous = num
      
        if self.length >= self.k:
            if num ==self.previous == self.value and self.no_value >= self.k:
                return True
            else:
                return False
        return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)