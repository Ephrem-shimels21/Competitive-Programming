class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        modulo_idx = defaultdict(int)
        modulo_idx[0] = -1
        minLen = len(nums)
        prefixSum = 0

        if target == 0:
            return 0

        for r in range(len(nums)):
            prefixSum += nums[r]
            mod = prefixSum % p
            diff = (mod - target + p) % p
            if diff in modulo_idx:
                minLen = min(minLen, r - modulo_idx[diff])
            
            modulo_idx[mod] = r
        
        if minLen != len(nums):
            return minLen
        return -1


        # target_remainder = sum(nums) % p
        # modP_indx = defaultdict(int)
        # minLen = float('inf')
        # remainders_map = defaultdict(int)
        # remainders = []
        # modp = 0
        # for idx, num in enumerate(nums):
        #     modp += num
        #     modp %= p
        #     remainders.append(modp)
        #     remainders_map[modp] = idx
            
        # for idx, remainder in enumerate(remainders):
        #     if remainder - target_remainder in remainders_map:
        #         minLen = min(minLen, idx - remainders_map[remainder - target_remainder] )
        
        # if minLen == float('inf'):
        #     return -1
        # return minLen
