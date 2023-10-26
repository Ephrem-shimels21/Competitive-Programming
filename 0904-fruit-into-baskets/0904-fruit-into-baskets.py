class Solution:
     def totalFruit(self, fruits: List[int]) -> int:
        left, count = 0 , {}
        max_fruits, res = 0, 0
        
        for right in range(len(fruits)):
            count[fruits[right]] = 1 + count.get(fruits[right],0)
            max_fruits += 1
            
            while len(count) > 2:
                count[fruits[left]] -= 1
                max_fruits -= 1
                if count[fruits[left]] == 0:
                    count.pop(fruits[left])
                left += 1

           
            res = max(res, max_fruits)
        return res
