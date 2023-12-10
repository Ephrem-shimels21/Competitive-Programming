class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        for index, chrr in enumerate(command):
            if chrr == "G":
                res += chrr
            elif chrr == "(":
                continue
            elif chrr == ")" and command[index - 1] == "(":
                res += "o"
            elif chrr == ")" and command[index - 1] != "(":
                res += "al"
        return res

        