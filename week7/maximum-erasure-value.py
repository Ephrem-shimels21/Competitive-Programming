class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_score = 0
        freq_dict = defaultdict(int)
        start = 0
        wind_sum = 0

        for end in range(len(nums)):
            if nums[end] in freq_dict:
                while nums[end] in freq_dict:
                    freq_dict[nums[start]] -= 1
                    wind_sum -= nums[start]
                    if  freq_dict[nums[start]] == 0:
                        freq_dict.pop(nums[start])
                    start += 1
                wind_sum += nums[end]
                freq_dict[nums[end]] += 1
            else:
                freq_dict[nums[end]] += 1
                wind_sum += nums[end]
            max_score = max(wind_sum, max_score)
            
        return max_score

        