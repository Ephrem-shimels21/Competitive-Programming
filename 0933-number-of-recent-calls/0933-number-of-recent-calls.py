class RecentCounter:

    def __init__(self):
        self.qeue = deque()
        

    def ping(self, t: int) -> int:
        self.qeue.append(t)
        
        while self.qeue[0] < t - 3000:
            self.qeue.popleft()
        
        return len(self.qeue)
            
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)