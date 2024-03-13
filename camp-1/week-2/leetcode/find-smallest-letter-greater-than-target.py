class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lef = 0
        ri = len(letters) - 1
        mid = (lef + ri) // 2
        result = letters[0]
       

        while lef <= ri:
            if letters[mid] <= target:
                lef = mid + 1
                mid = (lef + ri) // 2
            elif letters[mid] > target:
                result = letters[mid]
                ri = mid - 1
                mid = (lef + ri) // 2
        
        return result



        