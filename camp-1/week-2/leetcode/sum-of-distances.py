class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        left_idxs = defaultdict(int)
        right_idxs = defaultdict(int)
        idxAtleft = defaultdict(list)
        idxAtright = defaultdict(list)
        ans = [0] * len(nums)


        for idx, num in enumerate(nums):
            freq = len(idxAtleft[num])
            ans[idx] += (freq * idx) - left_idxs[num]

            idxAtleft[num].append(idx)
            left_idxs[num] += idx
        
        for idx in range(len(nums) - 1, -1, -1):
            num = nums[idx]
            freq = len(idxAtright[num])
            ans[idx] += (right_idxs[num] - (freq * idx))
            idxAtright[num].append(idx)
            right_idxs[num] += idx
        
        return ans
            
            

        