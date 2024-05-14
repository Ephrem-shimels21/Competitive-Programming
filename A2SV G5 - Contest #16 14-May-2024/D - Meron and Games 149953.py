# Problem: D - Meron and Games - https://codeforces.com/gym/523525/problem/D

from collections import Counter
import sys, threading


def main():
    n = int(input())
    arr = list(map(int, input().split()))

    arr_count = Counter(arr)
    unique = list(set(arr))
    unique.sort()

    def dp(idx):
        if idx >= len(unique):
            return 0

        if idx not in memo:
            take = 0
            if idx < len(unique) - 1:
                if unique[idx + 1] - 1 == unique[idx]:
                    take = arr_count[unique[idx]] * unique[idx] + dp(idx + 2)
                else:
                    take = arr_count[unique[idx]] * unique[idx] + dp(idx + 1)
            else:
                take = arr_count[unique[idx]] * unique[idx]

            leave = dp(idx + 1)
            memo[idx] = max(take, leave)

        return memo[idx]

    memo = {}
    print(dp(0))


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
