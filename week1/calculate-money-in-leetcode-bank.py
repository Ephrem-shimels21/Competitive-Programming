class Solution:
    def totalMoney(self, n: int) -> int:
        ans =  0
        no_7 = n//7
        reminder = n % 7
        starting_money = 1

        for _ in range(no_7):
            temp = starting_money
            for _ in range(7):
                ans += temp
                temp += 1
            starting_money += 1
        
        for _ in range(reminder):
            ans += starting_money
            starting_money += 1
        
        return ans
        