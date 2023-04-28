class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for ele in nums:
            if ele in count.keys():
                count[ele] += 1
            else:
                count[ele] = 1
       
        for freq in count.values():
            if freq >= 2:
                return True
        return False
        