# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0

        for operand in operations:
            if "+" in operand:
                x += 1
            else:
                x -= 1
        
        return x
        