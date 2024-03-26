class Robot:

    def __init__(self, width: int, height: int):
        self.positions = [((0, 0), "South")]
        for i in range(1, width):
            self.positions.append(((i, 0), "East"))
        
        for i in range(1, height):
            self.positions.append(((width - 1, i), "North"))
        
        for i in range(width - 2, -1, -1):
            self.positions.append(((i, height - 1), "West"))
        
        for i in range(height - 2, 0, -1):
            self.positions.append(((0, i), "South"))
        self.isOrigin = True
        self.i = 0
        
    def step(self, num: int) -> None:
        self.isOrigin = False
        self.i = (self.i + num) % len(self.positions)
       
        
        
    def getPos(self) -> List[int]:
        return self.positions[self.i][0]
        
    def getDir(self) -> str:
        return "East" if self.isOrigin else self.positions[self.i][1]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()