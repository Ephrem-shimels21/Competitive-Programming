class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        minn = float('inf')
        cant_good = set()
        cards_occ = defaultdict(list)

        for i in range(len(fronts)):
            cards_occ[fronts[i]].append(i)
        
        for num in cards_occ:
            is_there = False
            for idx in cards_occ[num]:
                if fronts[idx] == backs[idx]:
                    cant_good.add(num)
                    is_there = True
                if backs[idx] not in cant_good and backs[idx] != num and backs[idx] not in fronts:
                    minn = min(minn, backs[idx])
                    
            if not is_there and num not in cant_good:
                minn = min(minn, num)
        
        
        if minn == float('inf'):
            return 0
        return minn
                
                    