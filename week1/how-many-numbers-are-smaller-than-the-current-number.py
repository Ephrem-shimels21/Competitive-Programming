class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []

        # for num in nums:
        #     count = 0
        #     for num2 in nums:
        #         if num > num2:
        #             count += 1
        #     result.append(count)
        # return result

        nums_sorted = sorted(nums)
        greaters = {}

        for i in range(len(nums)):
            if nums_sorted[i] not in greaters:
                greaters[nums_sorted[i]] = i
        
        for num in nums:
            result.append(greaters[num])
        
        return result
        