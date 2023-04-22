class MyQueue:

    def __init__(self):
        self.stack1 = []
       
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        
    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True
        return False
    def pop(self) -> int:
        if self.empty() != True:
            return self.stack1.pop(0)
        
    def peek(self) -> int:
        if self.empty() != True:
            return self.stack1[0]       
        
  
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()