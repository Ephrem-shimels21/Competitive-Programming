class ATM:

    def __init__(self):
        self.note_id = {0 : 20, 1 : 50, 2 : 100, 3 : 200, 4 : 500}
        self.note_count = [0, 0, 0, 0, 0]
        self.notes = [500, 200, 100, 50, 20]
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for idx in range(len(banknotesCount)):
            self.note_count[idx] += banknotesCount[idx]

    def withdraw(self, amount: int) -> List[int]:
        ans = [0] * len(self.notes)
        
        for note in self.notes:
            idx = abs(4 - self.notes.index(note))
            total = self.note_count[idx]
           
            if amount >= note and total > 0:
                count = amount // note
                if total < count:
                    count = total
                amount = amount - (note * count)
                ans[idx] = count
            if amount == 0:
                break
       
        if amount == 0:
            for i in range(len(self.note_count)):
                self.note_count[i] -= ans[i]
            return ans
        else:
            return [-1]



        
        
        



# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)