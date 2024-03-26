class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(s, l, r):
            if l >= r:
                return 
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
            return swap(s, l, r)

        return swap(s, 0, len(s) - 1)
        