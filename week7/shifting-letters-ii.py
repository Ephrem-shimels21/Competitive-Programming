class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        total_shifts = [0] * (len(s) + 1)
        for shift in shifts:
            start, end, forward = shift
            if forward:
                total_shifts[start] += 1
                total_shifts[end + 1] -= 1
            else:
                total_shifts[start] -= 1
                total_shifts[end + 1] += 1
        
        for i in range(1, len(total_shifts)):
            total_shifts[i] = total_shifts[i - 1] + total_shifts[i]
        
        shifted_letters = []

        for idx, letter in enumerate(s):
            shifted_letter = chr(((ord(letter) - 97 + total_shifts[idx]) % 26) + 97)
            shifted_letters.append(shifted_letter)
        

        return ''.join(shifted_letters)


