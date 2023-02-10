class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
       if len(nums) is 1:
           return True
       dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
       for i in range(len(nums)):
           dp[i][i] = nums[i]
       for cur_len in range(1,len(nums)):
           for i in range(len(nums)-cur_len):
               j = i + cur_len
               dp[i][j] = max([sum(nums[i:j+1]) - dp[i][j-1], sum(nums[i:j+1]) - dp[i+1][j]])
               print(i,j,dp[i][j])
       return (dp[0][len(nums)-1] >= (sum(nums)/2))
        