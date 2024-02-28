class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        qeue = deque()
        deck.sort(reverse = True)

        for card in deck:
            if not qeue or len(qeue) == 1:
                qeue.appendleft(card)
            else:
                last = qeue.pop()
                qeue.appendleft(last)
                qeue.appendleft(card)
        
        return list(qeue)


        