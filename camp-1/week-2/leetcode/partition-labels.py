class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occ_idx = defaultdict(int)

        for i, char in enumerate(s):
            occ_idx[char] = i
            
        sizes = []
        partion_end = 0
        parition_size = 0

        for idx, letter in enumerate(s):
            partion_end = max(partion_end, occ_idx[letter])
            parition_size += 1
            if partion_end == idx:
                sizes.append(parition_size)
                parition_size = 0
        return sizes
        
        