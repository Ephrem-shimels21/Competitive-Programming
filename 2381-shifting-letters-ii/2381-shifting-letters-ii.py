class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        shiftAmount = [0] * len(s)
            
        for shift in shifts:
            if shift[-1]  == 0:
                shiftAmount[shift[0]] -= 1
                if shift[1] < (len(s) - 1):
                    shiftAmount[shift[1] + 1] += 1
            elif shift[-1] == 1:
                shiftAmount[shift[0]] += 1
                if shift[1] < len(s) - 1:
                    shiftAmount[shift[1] + 1] -= 1
        
        for index in range(1,len(shiftAmount)):
            shiftAmount[index] = shiftAmount[index] + shiftAmount[index - 1]
        
        shifted = []
        for i in range(len(s)):
            shift_value = shiftAmount[i] % 26
            shifted_char = chr((ord(s[i]) - ord('a') + shift_value) % 26 + ord('a'))
            shifted.append(shifted_char)

        return ''.join(shifted)
    