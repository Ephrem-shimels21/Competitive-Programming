class Solution:
    def minimumSteps(self, s: str) -> int:
        arr = list(s)
        if len(s) == 1:
            return 0
        fast, slow = len(s) - 2, len(s) - 1
        minsteps = 0
        while fast >= 0:
            if arr[slow] == "0" and arr[fast] == "1":
                arr[slow], arr[fast] = arr[fast], arr[slow]
                minsteps += (slow - fast)
                fast -= 1
                slow -= 1
            elif arr[slow] == "0" and  arr[fast] != "1":
                fast -= 1
            else:
                slow -= 1
                fast -= 1
        return minsteps

        