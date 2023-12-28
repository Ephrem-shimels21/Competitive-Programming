class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guarded = 0
        visited = set()
        walls_set = set((x,y) for x,y in walls)
        guard_set = set((x,y) for x,y in guards)
        for x,y in guards:
            b = y + 1
            while b < n :
                if (x,b) in walls_set or (x,b) in guard_set:
                    break                    
                elif (x,b) not in visited :
                    guarded += 1
                    visited.add((x,b))
                b += 1
            a = x + 1
            while a < m :
                if (a, y) in walls_set or (a,y) in guard_set:
                    break
                elif (a,y) not in visited:
                    guarded += 1
                    visited.add((a,y))
                a += 1
            a = x - 1
            while a >= 0:
                if (a, y) in walls_set or (a,y) in guard_set:
                    break
                elif (a,y) not in visited:
                    guarded += 1
                    visited.add((a,y))
                a -= 1
            b = y - 1
            while b >= 0:
                if (x,b) in walls_set or (x,b) in guard_set:
                    break
                elif (x,b) not in visited:
                    guarded += 1
                    visited.add((x,b))
                b -= 1
        return (m * n) - len(guards) - len(walls) - guarded


        