class Solution:
    def numberOfWays(self, s: str) -> int:
        pref_0 = []
        pref_1 = []
        
        for index, binary in enumerate(s):
            if pref_0 and binary == "0":
                pref_0.append(pref_0[index - 1] + 1)
                if pref_1:
                    pref_1.append(pref_1[index - 1])
                else:
                    pref_1.append(0)
            elif not pref_0 and binary == "0":
                pref_0.append(1)
                if pref_1:
                    pref_1.append(pref_1[index - 1])
                else:
                    pref_1.append(0)
            if pref_1 and binary == "1":
                pref_1.append(pref_1[index - 1] + 1)
                if pref_0:
                    pref_0.append(pref_0[index - 1])
                else:
                    pref_0.append(0)
            
            elif not pref_1 and binary == "1":
                pref_1.append(1)
                if pref_0:
                    pref_0.append(pref_0[index - 1])
                else:
                    pref_0.append(0)
        
        pref_01 = []
        pref_10 = []
        
        for i in range(len(s)):
            if pref_01 :
                if s[i] == "0":
                    pref_01.append(pref_01[i - 1])
                else:
                    pref_01.append(pref_01[i - 1] + pref_0[i])
            else:
                pref_01.append(0)
            
            if pref_10:
                if s[i] == "1":
                    pref_10.append(pref_10[i - 1])
                elif s[i] ==  "0":
                    pref_10.append(pref_10[i - 1] + pref_1[i])
            else:
                pref_10.append(0)
        count_010 = 0
        count_101 = 0
        for i in range(len(s)):
            if s[i] == "0":
                count_010 += pref_01[i]
            
            elif s[i] == "1":
                count_101 += pref_10[i]
        
        return count_010 + count_101
        
            
        