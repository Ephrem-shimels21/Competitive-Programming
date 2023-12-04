class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        re = nums[::]
        re.extend(nums)
        return re
        