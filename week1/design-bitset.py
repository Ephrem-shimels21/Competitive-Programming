class Bitset:

    def __init__(self, size: int):
        self.bit = [False for i in range(size)]
        self.bit_inv = [True for i in range(size)]
        self.total  = size
        self.one_bits = 0
        self.zero_bits =  size


    def fix(self, idx: int) -> None:
        if not self.bit[idx]:
            self.one_bits += 1
            self.zero_bits -= 1
        self.bit[idx] = True
        self.bit_inv[idx] = False
        
    def unfix(self, idx: int) -> None:
        if self.bit[idx]:
            self.one_bits -= 1
            self.zero_bits += 1
        self.bit[idx] = False
        self.bit_inv[idx] = True
        

    def flip(self) -> None:
        self.bit, self.bit_inv = self.bit_inv, self.bit
        self.one_bits , self.zero_bits = self.zero_bits, self.one_bits


    def all(self) -> bool:
        return self.one_bits == self.total
        

    def one(self) -> bool:
       return self.one_bits > 0

    def count(self) -> int:
        return self.one_bits
        

    def toString(self) -> str:
        ans = ""
        for boolean in self.bit:
            if boolean:
                ans += "1"
            else:
                ans += "0"
        return ans
       

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()