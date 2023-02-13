class Solution:
    def FindKthBit(self,n):
        if n == 1:
            return  "0"
        elif n != 1:
            outpuTemp=""
            for bits in self.FindKthBit(n-1):
                if bits == "1":
                    outpuTemp += "0"
                else:
                    bits= "1"
                    outpuTemp += bits
        return self.FindKthBit(n-1) + "1" + outpuTemp[::-1]
    
    def findKthBit(self, n: int, k: int) -> str:
        return self.FindKthBit(n)[k-1]