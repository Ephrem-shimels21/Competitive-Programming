class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        np = 0
        ty = 0

        while np <= len(name) and ty < len(typed):
            if np < len(name) and typed[ty] == name[np]:
                np += 1
                ty += 1
            elif typed[ty] == name[np - 1] and np != 0:
                ty += 1
            else:
                return False
       
        return np == len(name) and ty == len(typed)
          