class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        operands = "CD+"
        for op in operations:
            if op not in operands:
                stack.append(int(op))
            elif op == "C":
                stack.pop()
            elif op == "D":
                last = stack[-1]
                stack.append(last * 2)
            elif op  == "+":
                last = stack.pop()
                first = stack.pop()
                summ = last + first
                stack.append(first)
                stack.append(last)
                stack.append(summ)
        return sum(stack)
            