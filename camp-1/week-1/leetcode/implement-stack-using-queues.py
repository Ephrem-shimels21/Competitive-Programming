class MyStack:
     
    def __init__(self):
        self.stack = deque()
        
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.empty():
            return self.stack.pop()

    def top(self) -> int:
        if not self.empty():
            last = self.stack.pop()
            self.stack.append(last)
            return last
        
    def empty(self) -> bool:
        return len(self.stack) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()