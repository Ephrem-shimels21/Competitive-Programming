class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def find_sum(divisor):
            total = 0
            for num in nums:
                total += ceil(num /divisor)
            return total 

        l = 1
        r = max(nums)
        min_divisor = float('inf')

        while l <= r:
            mid = (l + r) // 2
            total = find_sum(mid)
            if total <= threshold:
                min_divisor = min(min_divisor, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return min_divisor
