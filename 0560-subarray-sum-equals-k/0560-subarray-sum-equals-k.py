class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
            count = 0
            sum = 0

            map = {}
            map[0] = 1

            for i in range(0, len(nums)):
                sum += nums[i]    

                if (sum - k) in map:
                    count += map.get(sum - k)
                map[sum] = map.get(sum, 0) + 1


            return count

 
        