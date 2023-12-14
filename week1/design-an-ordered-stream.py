class OrderedStream:
    def __init__(self, n: int):
        self.stream = {}
        self.next = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        ans = []
        if idKey == self.next:
            ans.append(value)
            self.next += 1
            idKey += 1
            while idKey in self.stream:
                ans.append(self.stream[idKey])
                self.next += 1
                idKey += 1
        else:
            self.stream[idKey] = value
        return ans



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)