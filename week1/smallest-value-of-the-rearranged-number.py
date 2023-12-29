class Solution:
    def smallestNumber(self, num: int) -> int:
        num_arr = list(str(abs(num)))
        if num < 0:
            num_arr.sort(reverse = True)
            return -1 * int("".join(num_arr))
        else:
            num_arr.sort()
            if int(num_arr[0]) == 0 and len(num_arr) > 1:
                for i in range(len(num_arr) - 1):
                    if int(num_arr[i]) == 0 and int(num_arr[i + 1]) != 0:
                        break 
                num_arr[0], num_arr[i + 1] = num_arr[i + 1], num_arr[0]

            return int("".join(num_arr))
        