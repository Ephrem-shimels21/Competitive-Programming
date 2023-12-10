class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        tx, ty = target[0], target[1]
        my_distance = max(tx, 0) - min(tx, 0) + max(ty, 0) - min(ty, 0)
        for ghost in ghosts:
            gx, gy = ghost[0], ghost[1]
            ghost_distance = max(gx,tx) - min(gx,tx) + max(gy, ty) - min(gy, ty)
            if ghost_distance <= my_distance:
                return False
        return True 
