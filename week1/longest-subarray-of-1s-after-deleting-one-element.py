class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        lon = 0
        wind = defaultdict(int)
        while r < (len(nums)):
            wind[nums[r]] += 1

            while wind[0] > 1:
                wind[nums[l]] -= 1
                if wind[nums[l]] == 0:
                    wind.pop(nums[l])
                l += 1
            lon = max(lon, r - l)
            r += 1
        return lon 