class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = ""

        for digit in digits:
            str_digits += str(digit)
        
        new_num = int(str_digits) + 1

        return [int(x) for x in str(new_num)]
        