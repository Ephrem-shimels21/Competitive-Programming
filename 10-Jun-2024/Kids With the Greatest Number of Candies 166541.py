# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        child_candy = {}

        for i in range(len(candies)):
            child_candy[i] = candies[i]
        candies.sort()
        res = []

        for key in child_candy:
            if child_candy[key] + extraCandies >= candies[-1]:
                res.append(True)
            else:
                res.append(False)
        return res
        