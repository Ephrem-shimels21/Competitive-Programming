class RecentCounter:

    def __init__(self):
        self.qeue = deque()
        self.count = 0
        

    def ping(self, t: int) -> int:
        self.qeue.append(t)
        self.count += 1
        
        while self.qeue[0] < t - 3000:
            self.qeue.popleft()
            self.count -= 1
        
        return self.count
            
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)