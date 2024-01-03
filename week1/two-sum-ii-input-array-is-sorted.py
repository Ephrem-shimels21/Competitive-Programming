class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        le = 0
        ri = len(numbers)-1
        ans=[]
        while le < ri:
            if numbers[le] + numbers[ri] == target:
                ans.append(le + 1)
                ans.append(ri + 1)
                return ans
            elif numbers[le] + numbers[ri] < target:
                le += 1
            elif numbers[le] + numbers[ri] > target:
                ri -=1
        return ans
            
        