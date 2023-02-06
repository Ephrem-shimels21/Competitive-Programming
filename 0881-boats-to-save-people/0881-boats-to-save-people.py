class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        hi, lo = len(people) - 1, 0
        while hi >= lo:
            if people[hi] + people[lo] <= limit:
                lo += 1
            hi -= 1
            res += 1
        return res
        