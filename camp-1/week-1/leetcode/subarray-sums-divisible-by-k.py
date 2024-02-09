class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cumulative_modK = defaultdict(int)
        modK = 0
        count = 0
        for num in nums:
            modK += num
            modK %= k
            if modK == 0 :
                count += 1
            if modK in cumulative_modK:
                count += cumulative_modK[modK]
            
            cumulative_modK[modK] += 1
        return count
            

        