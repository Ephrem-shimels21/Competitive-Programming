class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            if token[-1] not in '+-*/':
                s.append(int(token))
            else:
                n2 = s.pop()
                n1 = s.pop()
                if token == '+': n = n1 + n2
                elif token == '-': n = n1 - n2
                elif token == '*': n = n1 * n2
                elif token == '/': n = int(n1 / n2)
                s.append(n)
        return s[-1]
