class Solution:
    def bestClosingTime(self, customers: str) -> int:
        countY = customers.count("Y")
        prev_N_count = 0
        penalities = [countY]
        for come in customers:
            if come == "N":
                prev_N_count += 1
            else:
                countY -= 1
            
            penalities.append(prev_N_count + countY)
        
        minP = min(penalities)
        return penalities.index(minP)
