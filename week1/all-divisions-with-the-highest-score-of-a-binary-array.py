class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        max_count = 0
        total_ones = nums.count(1)
        indices = deque()
        ones = 0
        zeros = 0
        for idx,num in enumerate(nums):
            total = zeros + (total_ones - ones)
            if num == 0:
                zeros += 1
            else:
                ones += 1
            if total > max_count:
                indices.clear()
                indices.append(idx)
                max_count = total
            elif total == max_count:
                indices.append(idx)

        if zeros > max_count:
            indices.clear()
            indices.append(idx + 1)
        elif zeros == max_count:
            indices.append(idx + 1)
            
        return indices
        