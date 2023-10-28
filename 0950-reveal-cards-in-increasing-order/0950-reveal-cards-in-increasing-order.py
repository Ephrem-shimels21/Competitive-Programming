class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        qeue = deque(range(len(deck)))
        
        result = [0] * len(deck)
        
        for card in deck:
            result[qeue.popleft()] = card
            
            if qeue:
                qeue.append(qeue.popleft())
        return result