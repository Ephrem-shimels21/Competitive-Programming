class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        min_num = min(nums)
        counter = defaultdict(int)
        nums.sort()

        for i in range(len(nums)):
            counter[nums[i]] += 1
     
        operation = 0
        count = 0
        for key,value in counter.items():
     
            if key != min_num:
                operation += value * count
            count += 1
        return operation

        

        