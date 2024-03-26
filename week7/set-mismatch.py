class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_count =  Counter(nums)
        repeated = []
        not_in = []
        for i in range(1, len(nums) + 1):
            if i not in nums_count:
                not_in.append(i)
            elif nums_count[i] == 2:
                repeated.append(i)
        return repeated + not_in
        