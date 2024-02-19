class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        qeue = deque()

        time = 0
        for idx,ticket in enumerate(tickets):
            qeue.append((ticket, idx))
        
        while True:
            ticket, idx = qeue.popleft()
            ticket -= 1
            time  += 1
            if ticket != 0:
                qeue.append((ticket, idx))
            
            elif idx == k:
                return time
        



       