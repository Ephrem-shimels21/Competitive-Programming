class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        bl_wh_c = defaultdict(int)
        for i in range(k):
            bl_wh_c[blocks[i]] += 1
    
        l = 0
        min_change = float('inf')
        min_change = min(min_change, bl_wh_c["W"])
        for r in range(k, len(blocks)):
            min_change = min(min_change, bl_wh_c["W"])
            bl_wh_c[blocks[l]] -= 1
            bl_wh_c[blocks[r]] += 1
            if bl_wh_c[blocks[l]] == 0:
                bl_wh_c.pop(blocks[l])
            l += 1
        min_change = min(min_change, bl_wh_c["W"])
        return min_change
           

