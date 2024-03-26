class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        no_fives  = 0
        no_tens = 0
        for bill in bills:
            if bill == 5:
                no_fives += 1
            elif bill == 10:
                if not no_fives :
                    return False
                elif no_fives:
                    no_fives -= 1
                    no_tens += 1
            elif bill == 20:
                if no_fives and no_tens:
                    no_fives -= 1
                    no_tens -= 1
                elif no_fives >= 3:
                    no_fives -= 3
                else:
                    return False
        return True

        