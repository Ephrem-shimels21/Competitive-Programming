class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        operands = "CD+"
        for op in operations:
            if op not in operands:
                stack.append(int(op))
                total += int(op)
            elif op == "C":
                a = stack.pop()
                total -= a
            elif op == "D":
                last = stack[-1]
                double = last * 2
                stack.append(double)
                total += double
            elif op  == "+":
                last = stack.pop()
                first = stack.pop()
                summ = last + first
                stack.append(first)
                stack.append(last)
                stack.append(summ)
                total += summ
        return total
            