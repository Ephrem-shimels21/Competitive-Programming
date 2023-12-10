class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []

        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        
        ans = []
        i, j = 0, 0

        for _ in range(len(nums) // 2):
            ans.append(pos[j])
            ans.append(neg[i])
            i += 1
            j += 1
        return ans

            

            

            
                
                
            

        