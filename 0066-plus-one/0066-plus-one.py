class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # num = "".join(str(digit) for digit in digits)
        num = "".join(map(str,digits))
        num_int = int(num)
        num = str(num_int + 1)
        num = list(num)
        for index,digit in enumerate(num):
            num[index] = int(digit)
        
        return num
        