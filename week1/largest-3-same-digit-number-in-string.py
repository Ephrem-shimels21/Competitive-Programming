class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 0
        j = 3
        larger = 0
        ans = ""
        while j <= len(num):
            if len(set(num[i : j])) == 1:
                if int(num[i:j]) >= larger:
                    larger = int(num[i:j])
                    ans = num[i:j]
            i += 1
            j += 1
        return ans
        