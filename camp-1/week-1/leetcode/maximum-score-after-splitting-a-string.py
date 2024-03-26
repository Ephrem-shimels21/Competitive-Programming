class Solution:
    def maxScore(self, s: str) -> int:
        prefix_sum = []

        s_c = [int(bit) for bit in s]
        s_c = s_c[::-1]
        for i in range(1, len(s_c)):
            s_c[i] = s_c[i - 1] + s_c[i]
        
        s_c = s_c[::-1]
        
        zeros = 0
        maxx = 0
        for j in range(len(s) - 1):
            if s[j] == "0":
                zeros += 1
            maxx = max(maxx, zeros + s_c[j + 1])
            
        return maxx
        