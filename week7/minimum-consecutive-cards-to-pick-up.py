class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        min_len = float('inf')
        num_dict = defaultdict(int)

        for idx, card in enumerate(cards):
            if card in num_dict:
                min_len = min(min_len, idx - num_dict[card] + 1)
            num_dict[card] = idx
        
        if min_len == float('inf'):
            return -1
        return min_len
            
            