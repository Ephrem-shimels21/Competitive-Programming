class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.position = 0
        

    def visit(self, url: str) -> None:
        index = len(self.stack) - 1
        
        while index != self.position:
            self.stack.pop()
            index -= 1
        self.stack.append(url)
        self.position += 1
        

    def back(self, steps: int) -> str:
        self.position = max(self.position - steps, 0)
        return self.stack[self.position]
        
    def forward(self, steps: int) -> str:
        self.position = min(self.position + steps, len(self.stack) - 1)
        
        return self.stack[self.position]
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)