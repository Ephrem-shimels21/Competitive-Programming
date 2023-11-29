class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        first =  num / 3 - 1
   

        if first !=  num // 3 - 1:
            return []
        first = int(first)
        return [first, first + 1, first + 2]
        