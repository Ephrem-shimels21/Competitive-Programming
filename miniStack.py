class MinStack:
        def __init__(self):
            """
            initialize your data structure here.
            """
            self.stack = []
            self.index = -1
            self.min_stack = []
            self.min_index = -1
            self.min_value = float("inf")

        def push(self, x: int) -> None:
            if x < self.min_value:
                self.min_stack.append([x,1])
                self.min_value = x
                self.min_index += 1
            elif x == self.min_value:
                self.min_stack[self.min_index][1]+=1
            self.stack.append(x)
            self.index += 1

        def pop(self) -> None:
            if self.index < 0:
                return
            value = self.stack.pop()
            if value == self.min_value:
                self.min_stack[self.min_index][1] -= 1
            if self.min_stack[self.min_index][1] == 0:
                self.min_stack.pop()
                self.min_index -= 1
                if self.min_index != -1:
                    self.min_value = self.min_stack[self.min_index][0]
                else:
                    self.min_value = float("inf")
            if self.min_stack == -1: return
            self.index -= 1
        def top(self) -> int:
            if self.index < 0:
                return
            return self.stack[self.index]
        def getMin(self) -> int:
            return self.min_value
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()