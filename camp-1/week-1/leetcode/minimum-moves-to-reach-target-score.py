class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        min_operations = 0
        if not maxDoubles:
            return target - 1

        while target > 1:
            if not maxDoubles:
                min_operations += target - 1
                break
            else:
                if target % 2:
                    target -= 1
                    min_operations += 1
                else:
                    target //= 2
                    maxDoubles -= 1
                    min_operations += 1
        return min_operations
        